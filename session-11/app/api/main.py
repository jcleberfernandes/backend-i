from fastapi import FastAPI

from app.api.schemas import MeetingCreate, MeetingRead
from app.api.routers import action_items

app = FastAPI(title="Meeting Note Assistant API")

app.include_router(action_items.router)

DB: dict[str, dict] = {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/meetings")
def list_meetings() -> list[dict]:
    return list(DB.values())


@app.get("/meetings/{meeting_id}")
def get_meeting(meeting_id: str) -> dict:
    item = DB.get(meeting_id)
    if not item:
        return {"error": "Meeting not found"}
    return item


@app.post("/meetings", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate) -> MeetingRead:
    meeting_id = str(len(DB) + 1)
    meeting_data = {"id": meeting_id, **payload.model_dump()}
    DB[meeting_id] = meeting_data
    return MeetingRead(**meeting_data)
