# server.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse, Response
from typing import Dict, Set
import json
import os
import sys
import asyncio
import uvicorn
from datetime import datetime


app = FastAPI()

# Храним состояние по каждому татами
tatami_states: Dict[str, dict] = {}
# Подписчики WebSocket по каждому татами
tatami_clients: Dict[str, Set[WebSocket]] = {}

# --- Определяем папку, где лежит server.py / exe и наши HTML/JS ---
if getattr(sys, "frozen", False):
    # Если упаковано в exe (PyInstaller)
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # Обычный .py
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_PATH = os.path.join(BASE_DIR, "usko-overlay-server-html.html")
JS_PATH = os.path.join(BASE_DIR, "usko-overlay-server-script.js")

DELAY_SEC = 1.5  # общая задержка в секундах для обновления оверлея


async def broadcast_with_delay(tatami_id: str, payload: dict):
    """Отправляет состояние в WebSocket-клиенты с общей задержкой."""
    try:
        await asyncio.sleep(DELAY_SEC)
        for ws in list(tatami_clients.get(tatami_id, set())):
            try:
                await ws.send_text(json.dumps(payload, ensure_ascii=False))
            except Exception:
                # если что-то пошло не так с конкретным сокетом — просто пропускаем
                pass
    except Exception as e:
        print("_______Exception broadcast_with_delay:", e)

@app.get("/health")
async def health():
    """
    Быстрый health-check для табло судей.
    ДОЛЖЕН быть лёгким: без файлов, без ws, без state.
    """
    return {
        "ok": True,
        "service": "usko-overlay-server",
        "ts": datetime.utcnow().isoformat() + "Z",
        "delay_sec": DELAY_SEC,
        "tatami_states": len(tatami_states),
        "tatami_clients": {k: len(v) for k, v in tatami_clients.items()},
    }

@app.post("/api/state")
async def set_state(payload: dict, request: Request):
    """
    Приложение на татами дергает этот эндпоинт и передает
    полное состояние боя для конкретного tatami_id.
    """
    tatami_id = str(payload.get("tatami_id"))
    if not tatami_id:
        return {"status": "error", "message": "tatami_id is required"}

    tatami_states[tatami_id] = payload

    # Рассылаем всем WebSocket-клиентам оверлея для этого татами
    # создаём фоновую задачу, которая отправит обновление с задержкой
    asyncio.create_task(broadcast_with_delay(tatami_id, payload))

    print(f"[STATE] {datetime.now().strftime('%H:%M:%S')} overlay=http://{request.client.host}:8000/overlay/{tatami_id}")

    return {"status": "ok"}


@app.get("/overlay/{tatami_id}")
async def overlay(tatami_id: str, request: Request):
    """
    HTML-оверлей для OBS (Browser Source).
    Сам HTML лежит в файле usko-overlay-server-html.html.
    """
    try:
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        # Фолбэк, если файл не найден
        html = f"""
        <!DOCTYPE html>
        <html><head><meta charset="UTF-8"><title>USKO Overlay</title></head>
        <body style="background:#000;color:#fff;font-family:sans-serif;">
        <div>Ошибка: не найден файл usko-overlay-server-html.html</div>
        <div>{e}</div>
        </body></html>
        """

    print(f"[STATE] {datetime.now().strftime('%H:%M:%S')} overlay=http://{request.client.host}:8000/overlay/{tatami_id}")

    return HTMLResponse(html)


@app.get("/usko-overlay-server-script.js")
async def overlay_script():
    """
    JS-логика оверлея (подгружается из HTML через <script src="...">).
    """
    try:
        with open(JS_PATH, "r", encoding="utf-8") as f:
            js = f.read()
    except Exception as e:
        js = f'console.error("usko-overlay-server-script.js not found:", {json.dumps(str(e))});'
    return Response(js, media_type="application/javascript")


@app.websocket("/ws/{tatami_id}")
async def websocket_endpoint(websocket: WebSocket, tatami_id: str):
    await websocket.accept()
    tatami_clients.setdefault(tatami_id, set()).add(websocket)

    state = tatami_states.get(tatami_id)
    if state is not None:
        await websocket.send_text(json.dumps(state, ensure_ascii=False))

    try:
        while True:
            # держим соединение, нам не нужны сообщения от клиента
            await websocket.receive_text()
    except WebSocketDisconnect:
        tatami_clients[tatami_id].discard(websocket)
        if not tatami_clients[tatami_id]:
            tatami_clients.pop(tatami_id, None)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
