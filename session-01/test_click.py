import click


@click.group()
def cli():
    pass


@cli.command("hi")
def hi():
    click.echo("Hello from Click!")


if __name__ == "__main__":
    cli()
