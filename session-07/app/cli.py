import typer
from app.services.meeting_service import (
    create_meeting,
    list_meetings,
    get_meeting,
    delete_meeting,
)
from app.services.report_service import summary
from app.services.memory_store import meetings
from app.core.logging_config import configure_logging
from app.core.errors import ValidationError, NotFoundError
from app.core.validators import validate_iso_date

configure_logging()

app = typer.Typer()


@app.command("create-meeting")
def create_meeting_cmd(
    title: str = typer.Option(..., "--title"),
    date: str = typer.Option(..., "--date"),
    owner: str = typer.Option(..., "--owner"),
) -> None:
    try:
        validate_iso_date(date)
        meeting = create_meeting(title, date, owner)
        typer.echo(f"Created: {meeting.id}")
    except ValidationError as exc:
        typer.echo(f"Validation error: {exc}")
        raise typer.Exit(code=2)


@app.command("list-meetings")
def list_meetings_cmd() -> None:
    for m in list_meetings():
        typer.echo(f"{m.id} | {m.date} | {m.title}")


@app.command("show-meeting")
def show_meeting_cmd(id: str = typer.Option(..., "--id")) -> None:
    try:
        meeting = get_meeting(id)
        typer.echo(f"ID: {meeting.id}")
        typer.echo(f"Title: {meeting.title}")
        typer.echo(f"Date: {meeting.date}")
        typer.echo(f"Owner: {meeting.owner}")
    except NotFoundError as exc:
        typer.echo(f"Error: {exc}")
        raise typer.Exit(code=1)


@app.command("delete-meeting")
def delete_meeting_cmd(id: str = typer.Option(..., "--id")) -> None:
    try:
        delete_meeting(id)
        typer.echo(f"Deleted meeting {id}")
    except NotFoundError as exc:
        typer.echo(f"Error: {exc}")
        raise typer.Exit(code=1)


@app.command("summary")
def summary_cmd() -> None:
    result = summary(meetings)
    typer.echo(f"Meetings: {result['meetings']}")
    typer.echo(f"Action Items: {result['action_items']}")


if __name__ == "__main__":
    app()
