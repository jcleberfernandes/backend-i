from typer import Typer
import uvicorn
from src.api.main import app



cli = Typer()

@cli.command()
def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    cli()
