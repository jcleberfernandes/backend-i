from fastapi import FastAPI
from uuid import uuid4
from src.models.meeting_models import Meeting
from src.storage.meeting_storage import meeting_storage


api= FastAPI()






@api.post("/create-meeting", response_model = Meeting)
def create_meeting(meeting: Meeting):
    meeting_id = uuid4()
    meeting_storage[meeting_id] = meeting





@api.get("/get-meeting")
def get_meetings():
    return meeting_storage




#GET = Obtém dados do projeto;
# POST = Cria novos;
# PUT = Atualiza existentes; 
# DELETE = Remove-os.