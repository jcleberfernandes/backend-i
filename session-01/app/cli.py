import typer

app = typer.Typer()


@app.command("hi")
def hi() -> None:
    typer.echo("Hello from Typer!!!")


@app.command("create-meeting")
def create_meeting(title: str, date: str, owner: str) -> None:
    typer.echo(f"Meeting created: {title} on {date} by {owner}")


if __name__ == "__main__":
    app()
