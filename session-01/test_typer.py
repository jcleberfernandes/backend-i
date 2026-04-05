import typer

app = typer.Typer()


@app.command("hi")
def hi():
    typer.echo("Hello from Typer!!!")


if __name__ == "__main__":
    app()
