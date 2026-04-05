from fastapi import FastAPI

from app.api.schemas import MeetingCreate, MeetingRead

app = FastAPI(title="Meeting Note Assistant API")

from app.api.routers import meetings

app.include_router(meetings.router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/meetings")
def list_meetings() -> list[dict]:
    from app.api.routers.meetings import DB

    return list(DB.values())


@app.get("/meetings/{meeting_id}")
def get_meeting(meeting_id: str) -> dict:
    from app.api.routers.meetings import DB

    item = DB.get(meeting_id)
    if not item:
        return {"error": "Meeting not found"}
    return item


@app.post("/meetings", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate) -> MeetingRead:
    from app.api.routers.meetings import DB

    meeting_id = str(len(DB) + 1)
    meeting_data = {"id": meeting_id, **payload.model_dump()}
    DB[meeting_id] = meeting_data
    return MeetingRead(**meeting_data)
