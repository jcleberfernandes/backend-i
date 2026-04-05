import json
from dataclasses import asdict
from pathlib import Path
from app.domain.models import Meeting, ActionItem

DB = Path("data/meetings.json")


def save_meetings(items: list[Meeting]) -> None:
    DB.parent.mkdir(parents=True, exist_ok=True)
    DB.write_text(json.dumps([asdict(m) for m in items], indent=2), encoding="utf-8")


def load_meetings() -> list[Meeting]:
    if not DB.exists():
        return []
    data = json.loads(DB.read_text(encoding="utf-8"))
    meetings: list[Meeting] = []
    for m in data:
        actions = [ActionItem(**a) for a in m.get("action_items", [])]
        meetings.append(Meeting(**{**m, "action_items": actions}))
    return meetings
