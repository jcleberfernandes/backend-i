import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import typer
from app.services.meeting_service import create_meeting, list_meetings
from app.storage.json_repository import save_meetings, load_meetings

app = typer.Typer()

MEETINGS = load_meetings()


@app.command("create-meeting")
def create_meeting_cmd(title: str, date: str, owner: str) -> None:
    global MEETINGS
    meeting = create_meeting(title, date, owner)
    MEETINGS.append(meeting)
    save_meetings(MEETINGS)
    typer.echo(f"Created: {meeting.id}")


@app.command("list-meetings")
def list_meetings_cmd() -> None:
    for m in list_meetings():
        typer.echo(f"{m.id} | {m.date} | {m.title}")


if __name__ == "__main__":
    app()
