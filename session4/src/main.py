import typer
import services

cli = typer.Typer()


@cli.command()
def create(
    title:str,
    owner:str,
    date:str)->None:
    services.meeting.create(title, owner, date)
    typer.echo("meeting created")
    


if __name__ == "__main__":
    cli()

