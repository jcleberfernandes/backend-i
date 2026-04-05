import typer
from app.services.meeting_service import create_meeting, list_meetings

app = typer.Typer()


@app.command("create-meeting")
def create_meeting_cmd(
    title: str = typer.Option(..., "--title"),
    date: str = typer.Option(..., "--date"),
    owner: str = typer.Option(..., "--owner"),
) -> None:
    meeting = create_meeting(title, date, owner)
    typer.echo(f"Created: {meeting.id}")


@app.command("list-meetings")
def list_meetings_cmd() -> None:
    for m in list_meetings():
        typer.echo(f"{m.id} | {m.date} | {m.title}")


if __name__ == "__main__":
    app()
