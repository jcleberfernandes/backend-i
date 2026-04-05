from fastapi import FastAPI
from app.api.routers import meetings, action_items

app = FastAPI(title="Meeting Note Assistant API")

app.include_router(meetings.router)
app.include_router(action_items.router)


@app.get("/health")
def health():
    return {"status": "ok"}
