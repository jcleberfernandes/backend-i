from fastapi import APIRouter, HTTPException
from app.api.schemas import ActionItemCreate, ActionItemRead

router = APIRouter(prefix="/meetings", tags=["action-items"])
ACTION_DB: dict[str, list[dict]] = {}


@router.post(
    "/{meeting_id}/action-items", response_model=ActionItemRead, status_code=201
)
def create_action_item(meeting_id: str, payload: ActionItemCreate):
    item = {"id": str(len(ACTION_DB.get(meeting_id, [])) + 1), **payload.model_dump()}
    ACTION_DB.setdefault(meeting_id, []).append(item)
    return ActionItemRead(**item)


@router.get("/{meeting_id}/action-items")
def list_action_items(meeting_id: str):
    return ACTION_DB.get(meeting_id, [])
