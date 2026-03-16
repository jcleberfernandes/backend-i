
import json
from typer import Typer
from api.main import app
import uvicorn
from api.models import Meeting
app = Typer(name="MEETING")

def adiconar_meeting(meeting: Meeting):
    with open("meeting.json", "w") as f:
      json.dump(meeting.dict(), f)
      
def ler_meeting() -> Meeting:
    with open("meeting.json", "r") as f:
      data = json.load(f)
      return Meeting(**data)
    

@app.command("run")  
def run():
  uvicorn.run(app)


@app.command("request")
def request():
  ...

if __name__ == "__main__":
    app() 
