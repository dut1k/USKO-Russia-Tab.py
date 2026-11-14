# server.py
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Dict, Set
import json
import os
import re
import sys
import asyncio
import uvicorn
import logging
from collections import defaultdict, namedtuple
from datetime import datetime, timedelta
from hmac import compare_digest
from pathlib import Path
from tempfile import NamedTemporaryFile
from time import monotonic
from competition_results import save_event

app = FastAPI()
logger = logging.getLogger("usko.server")
connections = logging.getLogger("usko.connections")

tatami_states: Dict[str, dict] = {}
tatami_clients: Dict[str, Set[WebSocket]] = {}

# --- где лежит exe/py ---
if getattr(sys, "frozen", False) and not os.path.isdir(os.path.join(os.path.dirname(__file__), "assets")):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
HTML_PATH = os.path.join(ASSETS_DIR, "usko-overlay-server-html.html")

DELAY_SEC = 1.0
ACTIVE_SEC = 20
LEGACY_ACTIVE_SEC = 30
MAX_DELAY_SEC = 3600
delay_file = None
delay_token = ""
delay_rows = {}
last_seen = {}
retired_sessions = defaultdict(set)
Presence = namedtuple("Presence", ("tatami_id", "seen_at", "session_id", "seen_wall", "disconnected"))
received_revision = defaultdict(int)
published_revision = defaultdict(int)
publish_locks = defaultdict(asyncio.Lock)
pending_updates = {}
results_file = None


def configure_delays(path, token=""):
    global delay_file, delay_token, delay_rows
    delay_file = Path(path)
    delay_token = token
    try:
        delay_rows = json.loads(delay_file.read_text(encoding="utf-8"))
        if not isinstance(delay_rows, dict) or any(
            not isinstance(row, dict) or not isinstance(row.get("tatami_id"), str)
            or not valid_delay(row.get("delay_sec")) for row in delay_rows.values()
        ):
            raise ValueError("Некорректный формат настроек задержки")
    except FileNotFoundError:
        delay_rows = {}
    except (OSError, ValueError):
        logger.exception("Не удалось прочитать настройки задержки")
        delay_rows = {}


def valid_delay(value):
    return type(value) in (int, float) and 0 <= value <= MAX_DELAY_SEC


def save_delays(rows):
    global delay_rows
    if delay_file is not None:
        # Замена целого файла сохраняет предыдущую версию при ошибке записи.
        temporary = None
        try:
            delay_file.parent.mkdir(parents=True, exist_ok=True)
            with NamedTemporaryFile(mode="w", encoding="utf-8", dir=delay_file.parent,
                                    delete=False) as stream:
                temporary = Path(stream.name)
                json.dump(rows, stream, ensure_ascii=False, indent=2)
            temporary.replace(delay_file)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    delay_rows = rows


def check_delay_access(request):
    # Интерфейс управления доступен окну сервера через loopback с ключом сеанса.
    token = request.headers.get("X-USKO-Delay-Token", "").encode("utf-8")
    if (request.client.host != "127.0.0.1" or not delay_token
            or not compare_digest(token, delay_token.encode("ascii"))):
        raise HTTPException(status_code=403)


def presence_active(presence, now):
    if presence is None or presence.disconnected:
        return False
    timeout = ACTIVE_SEC if presence.session_id else LEGACY_ACTIVE_SEC
    return now - presence.seen_at < timeout


@app.get("/api/delays")
async def list_delays(request: Request):
    check_delay_access(request)
    now = monotonic()
    return [dict(row, ip=ip, active=presence_active(last_seen.get(ip), now))
            for ip, row in sorted(delay_rows.items())]


@app.get("/api/session-tables")
async def session_tables(request: Request):
    check_delay_access(request)
    now = monotonic()
    # Список сеанса живёт в памяти и не зависит от удаления настроек IP.
    rows = []
    for ip, presence in last_seen.items():
        active = presence_active(presence, now)
        row = dict(ip=ip, tatami_id=presence.tatami_id, active=active)
        if not active:
            timeout = ACTIVE_SEC if presence.session_id else LEGACY_ACTIVE_SEC
            when = presence.disconnected or presence.seen_wall + timedelta(seconds=timeout)
            row["disconnected_at"] = when.isoformat(timespec="seconds")
        rows.append(row)
    return rows


@app.post("/api/delays")
async def change_delay(payload: dict, request: Request):
    check_delay_access(request)
    ip = payload.get("ip")
    if not isinstance(ip, str) or ip not in delay_rows:
        raise HTTPException(status_code=404, detail="Стол отсутствует в списке")
    rows = delay_rows.copy()
    if payload.get("delete") is True:
        del rows[ip]
    else:
        delay = payload.get("delay_sec")
        if not valid_delay(delay):
            raise HTTPException(status_code=422, detail="Задержка должна быть от 0 до 3600 секунд")
        rows[ip] = dict(rows[ip], delay_sec=delay)
    try:
        save_delays(rows)
    except OSError:
        logger.exception("Не удалось сохранить настройки задержки")
        raise HTTPException(status_code=500, detail="Не удалось сохранить настройки задержки")
    return await list_delays(request)

# --- раздача статики /assets/... (fonts, regions, html, js) ---
app.mount("/assets", StaticFiles(directory=ASSETS_DIR, html=False), name="assets")


def merge_state(previous, patch):
    merged = previous.copy() if isinstance(previous, dict) else {}
    for key, value in patch.items():
        merged[key] = merge_state(merged.get(key), value) if isinstance(value, dict) else value
    return merged


def ensure_delay_row(ip, tatami_id):
    previous = delay_rows.get(ip, {"delay_sec": DELAY_SEC})
    if previous.get("tatami_id") != tatami_id and (delay_token or delay_file is not None):
        try:
            save_delays({**delay_rows, ip: dict(previous, tatami_id=tatami_id)})
        except OSError:
            logger.exception("Не удалось сохранить данные стола %s", ip)
    return previous["delay_sec"]


@app.post("/api/presence/{action}")
async def update_presence(action: str, payload: dict, request: Request):
    session_id = payload.get("session_id")
    tatami = payload.get("tatami_id")
    if action not in ("heartbeat", "disconnect"):
        raise HTTPException(status_code=404)
    if (not isinstance(session_id, str) or not re.fullmatch(r"[0-9a-f]{32}", session_id)
            or not isinstance(tatami, str) or not tatami.strip()):
        raise HTTPException(status_code=422)
    ip = request.client.host
    current = last_seen.get(ip)
    if action == "disconnect":
        # Запоминаем закрытие, даже если отправленный перед ним heartbeat
        # задержался. Чужой сеанс с тем же IP закрывать нельзя.
        retired_sessions[ip].add(session_id)
        if current is not None and current.session_id == session_id:
            if not current.disconnected:
                last_seen[ip] = current._replace(disconnected=datetime.now().astimezone())
    elif session_id not in retired_sessions[ip]:
        if current is not None and current.session_id and current.session_id != session_id:
            retired_sessions[ip].add(current.session_id)
        last_seen[ip] = Presence(tatami, monotonic(), session_id, datetime.now().astimezone(), None)
        ensure_delay_row(ip, tatami)
    return {"status": "ok"}


async def broadcast_with_delay(tatami_id: str, payload: dict, revision: int, due: float, previous):
    # Частичная оценка в ката зависит от ранее отправленных данных участника.
    # Она ждёт предыдущее обновление, даже если для её IP уже уменьшили задержку.
    if previous is not None:
        await previous
    remaining = due - monotonic()
    if remaining > 0:
        await asyncio.sleep(remaining)
    async with publish_locks[tatami_id]:
        # После уменьшения задержки новое состояние может обогнать старое.
        # Старое тогда пропускаем, чтобы счёт или победитель не откатились.
        if revision <= published_revision[tatami_id]:
            return
        published_revision[tatami_id] = revision
        if payload.get("partial"):
            snapshot = merge_state(tatami_states.get(tatami_id), payload)
            snapshot.pop("partial", None)
        else:
            snapshot = payload
        tatami_states[tatami_id] = snapshot
        for ws in list(tatami_clients.get(tatami_id, set())):
            try:
                await ws.send_text(json.dumps(payload, ensure_ascii=False))
            except Exception:
                logger.warning("Ошибка отправки WebSocket: татами %s", tatami_id, exc_info=True)


@app.get("/health")
async def health():
    return {
        "ok": True,
        "service": "usko-overlay-server",
        "ts": datetime.utcnow().isoformat() + "Z",
        "delay_sec": DELAY_SEC,
        "tatami_states": len(received_revision),
        "tatami_clients": {k: len(v) for k, v in tatami_clients.items()},
    }


@app.post("/api/state")
async def set_state(payload: dict, request: Request):
    raw_tatami = payload.get("tatami_id")
    if not isinstance(raw_tatami, (str, int)) or not str(raw_tatami).strip():
        return {"status": "error", "message": "tatami_id is required"}
    tatami_id = str(raw_tatami)
    # Архивные данные предназначены только для серверной консоли.
    result_event = payload.pop("result_event", None)

    if tatami_id not in received_revision:
        connections.info("Получены первые данные табло: татами %s, адрес %s", tatami_id, request.client.host)
    ip = request.client.host
    now = monotonic()
    current = last_seen.get(ip)
    # Рабочие запросы подтверждают связь даже при пропусках heartbeat.
    # Идентификатор позволяет отличить запрос из уже закрытого сеанса.
    session_id = request.headers.get("X-USKO-Session", "")
    if not re.fullmatch(r"[0-9a-f]{32}", session_id):
        session_id = None
    if session_id in retired_sessions.get(ip, ()) or (
        current and current.session_id and session_id != current.session_id
        and (session_id or current.disconnected)
    ):
        delay = delay_rows.get(ip, {}).get("delay_sec", DELAY_SEC)
    else:
        session_id = session_id or (current.session_id if current else None)
        delay = ensure_delay_row(ip, tatami_id)
        last_seen[ip] = Presence(tatami_id, now, session_id, datetime.now().astimezone(), None)
    received_revision[tatami_id] += 1
    dependency = pending_updates.get(tatami_id) if payload.get("partial") else None
    pending_updates[tatami_id] = asyncio.create_task(
        broadcast_with_delay(tatami_id, payload, received_revision[tatami_id],
                             now + delay, dependency))

    # Частые обновления таймера не засоряют обычный журнал. Полные сообщения
    # с ФИО не записываем; для диагностики достаточно татами и источника.
    logger.debug("STATE: татами %s, источник %s", tatami_id, request.client.host)
    if result_event is not None and results_file is not None:
        try:
            await asyncio.to_thread(save_event, results_file, tatami_id,
                                    payload.get("overlay_seq"), result_event)
        except (ValueError, TypeError, AttributeError, KeyError):
            logger.warning("Некорректное событие результата: татами %s", tatami_id)
            return {"status": "ok", "result_saved": False}
        except Exception:
            logger.exception("Не удалось записать результат: татами %s", tatami_id)
            return {"status": "ok", "result_saved": False}
        return {"status": "ok", "result_saved": True}
    return {"status": "ok"}


@app.get("/overlay/{tatami_id}")
async def overlay(tatami_id: str, request: Request):
    try:
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        logger.exception("Не удалось загрузить HTML оверлея")
        html = f"""
        <!DOCTYPE html>
        <html><head><meta charset="UTF-8"><title>USKO Overlay</title></head>
        <body style="background:#000;color:#fff;font-family:sans-serif;">
        <div>Ошибка: не найден файл assets/usko-overlay-server-html.html</div>
        <div>{e}</div>
        </body></html>
        """

    connections.info("Открыт оверлей: татами %s, адрес %s", tatami_id, request.client.host)
    return HTMLResponse(html)


@app.websocket("/ws/{tatami_id}")
async def websocket_endpoint(websocket: WebSocket, tatami_id: str):
    await websocket.accept()
    connections.info("WebSocket подключён: татами %s", tatami_id)

    try:
        async with publish_locks[tatami_id]:
            tatami_clients.setdefault(tatami_id, set()).add(websocket)
            # При переподключении показываем состояние, уже вышедшее в эфир.
            state = tatami_states.get(tatami_id)
            if state is not None:
                await websocket.send_text(json.dumps(state, ensure_ascii=False))
        while True:
            # соединение держим; сообщения от клиента не нужны
            await websocket.receive_text()
    except WebSocketDisconnect:
        pass
    finally:
        # Очистка нужна и при остановке серверного процесса, и при ошибке
        # первоначальной отправки, а не только при штатном отключении OBS.
        clients = tatami_clients.get(tatami_id)
        if clients is not None:
            clients.discard(websocket)
            if not clients:
                tatami_clients.pop(tatami_id, None)
        connections.info("WebSocket отключён: татами %s", tatami_id)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
