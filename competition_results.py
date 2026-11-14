"""Архив событий соревнований, общий для сервера и его консоли."""
from contextlib import closing
from datetime import datetime
import json
import sqlite3
from uuid import UUID


MODES = {"kumite": "Кумите", "kata_qual": "Ката по флажкам", "kata_final": "Ката финал"}
SIDES = ("aka", "siro")


def save_event(path, tatami, revision, event):
    # Один снимок на действие судьи. Параллельные HTTP-запросы могут прийти
    # в обратном порядке, поэтому в архиве порядок задаёт номер с табло.
    if not isinstance(event, dict) or type(revision) is not int or not 0 < revision < 2**63:
        raise ValueError("Некорректное событие результата")
    performance = UUID(event.get("id", "")).hex
    mode = event.get("mode")
    kind = event.get("kind")
    timestamp = datetime.fromisoformat(event.get("time", ""))
    if mode not in MODES or timestamp.utcoffset() is None:
        raise ValueError("Некорректный вид соревнований или время")
    if kind != "result" and (kind != "change" or mode != "kumite"):
        raise ValueError("Некорректный вид события")
    if kind == "result" and mode != "kata_final" and event.get("winner") not in SIDES:
        raise ValueError("Не указан победитель")
    sides = ("aka",) if mode == "kata_final" else SIDES
    snapshot = {key: event[key] for key in ("id", "mode", "kind", "time", "category")}
    if not isinstance(snapshot["category"], str):
        raise ValueError("Некорректная категория")
    for side in sides:
        athlete = event[side]
        snapshot[side] = {key: athlete[key] for key in ("name", "region")}
        if not all(isinstance(value, str) for value in snapshot[side].values()):
            raise ValueError("Некорректные данные участника")
        if mode == "kumite":
            score = athlete["score"]
            int(score or 0)
            penalties = {key: athlete["penalties"][key] for key in ("hm", "j")}
            if not all(isinstance(value, str) for value in penalties.values()):
                raise ValueError("Некорректное нарушение")
            snapshot[side].update(score=score, penalties=penalties)
    if mode == "kumite":
        seconds = event["remaining_sec"]
        if seconds is not None and (type(seconds) is not int or not 0 <= seconds < 3600):
            raise ValueError("Некорректное время поединка")
        snapshot["remaining_sec"] = seconds
    if mode == "kata_final":
        scores = {f"ref{index}": event["scores"][f"ref{index}"] for index in range(1, 8)}
        excluded = event["excluded"]
        if not all(isinstance(value, str) for value in scores.values()):
            raise ValueError("Некорректные оценки")
        if not isinstance(excluded, list) or any(type(i) is not int or not 1 <= i <= 7 for i in excluded):
            raise ValueError("Некорректные номера исключённых оценок")
        total = event["total"]
        if not isinstance(total, str):
            raise ValueError("Некорректная сумма")
        float(total)
        snapshot.update(scores=scores, excluded=excluded, total=total)
    elif kind == "result":
        snapshot["winner"] = event["winner"]

    # SQLite отделяет архив от ротируемых технических логов. Транзакция
    # сохраняет событие целиком, первичный ключ исключает дубли при повторе.
    with closing(sqlite3.connect(path)) as db, db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS result_events (
                tatami TEXT NOT NULL, performance TEXT NOT NULL, revision INTEGER NOT NULL,
                kind TEXT NOT NULL, snapshot TEXT NOT NULL,
                PRIMARY KEY (tatami, performance, revision)
            ) WITHOUT ROWID
        """)
        db.execute("INSERT OR IGNORE INTO result_events VALUES (?, ?, ?, ?, ?)",
                   (tatami, performance, revision, kind, json.dumps(snapshot, ensure_ascii=False)))


def load_results(path):
    if not path.is_file():
        return []
    # Читатель может открыться одновременно с первой записью в новый файл.
    with closing(sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True, timeout=0.05)) as db:
        if not db.execute("SELECT 1 FROM sqlite_master WHERE name = 'result_events'").fetchone():
            return []
        rows = db.execute("""
            SELECT tatami, performance, revision, kind, snapshot FROM result_events
            ORDER BY tatami, performance, revision
        """).fetchall()

    results = {}
    history = {}
    for tatami, performance, revision, kind, snapshot in rows:
        key = tatami, performance
        event = json.loads(snapshot)
        # Изменение счёта без выбора победителя всё равно относится к бою.
        # Если итог уже зафиксирован, карточка сохраняет его до нового решения.
        if kind == "result" or results.get(key, {}).get("kind") != "result":
            results[key] = dict(event, key=key, tatami_id=tatami, revision=revision)
        if event["mode"] == "kumite":
            history.setdefault(key, []).append((revision, event))

    for key, result in results.items():
        if key in history:
            result["timeline"] = kumite_timeline(
                event for revision, event in history[key] if revision <= result["revision"]
            )
    return sorted(results.values(), key=lambda result: datetime.fromisoformat(result["time"]), reverse=True)


def kumite_timeline(events):
    # Счёт и ступени штрафов сравниваем со снимком предыдущего действия,
    # а остаток времени берём из снимка именно этого действия.
    previous = {}
    timeline = []
    for event in events:
        for side in SIDES:
            before = previous.get(side, {})
            after = event[side]
            score = int(after["score"] or 0)
            delta = score - int(before.get("score") or 0)
            if delta:
                timeline.append((side, f"{delta:+d} (счёт {score})", event["remaining_sec"]))
            for penalty, label in (("hm", "H/M"), ("j", "J")):
                value = after["penalties"].get(penalty) or ""
                if value != (before.get("penalties", {}).get(penalty) or ""):
                    action = f"нарушение {label} · {value}" if value else f"отмена нарушения {label}"
                    timeline.append((side, action, event["remaining_sec"]))
        previous = event
    return timeline
