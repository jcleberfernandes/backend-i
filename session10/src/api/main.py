from fastapi import FastAPI
from uuid import uuid4
from src.models.meeting_models import Meeting, MeetingSummary
from src.storage.meeting_storage import meeting_storage
from src.services.ollama_services import generate_summary

app= FastAPI()






@app.post("/create-meeting", response_model=MeetingSummary)
def create_meeting(meeting: Meeting):
    summary = generate_summary(meeting)
    meeting_id = uuid4()
    
    meeting_sumary = MeetingSummary(
        id=meeting_id,
        summary=summary
    )
    
    meeting_storage[meeting_id] = summary
    return meeting_sumary
    



@app.get("/get-meeting")
def get_meetings():
    return meeting_storage




#GET = Obtém dados do projeto;
# POST = Cria novos;
# PUT = Atualiza existentes; 
# DELETE = Remove-os.