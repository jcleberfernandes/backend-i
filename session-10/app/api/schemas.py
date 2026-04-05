from pydantic import BaseModel, Field


class MeetingCreate(BaseModel):
    title: str = Field(min_length=3)
    date: str
    owner: str = Field(min_length=2)


class MeetingRead(MeetingCreate):
    id: str


class MeetingUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3)
    date: str | None = None
    owner: str | None = Field(default=None, min_length=2)
