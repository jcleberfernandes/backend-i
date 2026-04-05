from fastapi import APIRouter, HTTPException, Query
from app.api.schemas import MeetingCreate, MeetingRead, MeetingUpdate

router = APIRouter(prefix="/meetings", tags=["meetings"])
DB: dict[str, dict] = {}


@router.post("", response_model=MeetingRead, status_code=201)
def create_meeting(payload: MeetingCreate):
    meeting_id = str(len(DB) + 1)
    DB[meeting_id] = {"id": meeting_id, **payload.model_dump()}
    return DB[meeting_id]


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_meeting(meeting_id: str):
    item = DB.get(meeting_id)
    if not item:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return item


@router.put("/{meeting_id}", response_model=MeetingRead)
def update_meeting(meeting_id: str, payload: MeetingUpdate):
    if meeting_id not in DB:
        raise HTTPException(status_code=404, detail="Meeting not found")
    DB[meeting_id] = {"id": meeting_id, **payload.model_dump()}
    return DB[meeting_id]


@router.get("")
def list_meetings(
    owner: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    ordering: str = Query(default="date"),
):
    items = list(DB.values())
    if owner:
        items = [m for m in items if m["owner"] == owner]

    if ordering == "date":
        items = sorted(items, key=lambda x: x["date"])
    elif ordering == "-date":
        items = sorted(items, key=lambda x: x["date"], reverse=True)
    elif ordering == "title":
        items = sorted(items, key=lambda x: x.get("title", ""))
    elif ordering == "-title":
        items = sorted(items, key=lambda x: x.get("title", ""), reverse=True)

    return {
        "total": len(items),
        "items": items[offset : offset + limit],
        "limit": limit,
        "offset": offset,
    }
