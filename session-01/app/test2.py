import typer

app = typer.Typer()


@app.command("hi")
def hi() -> None:
    typer.echo("Hello from Typer!!!")


app()
