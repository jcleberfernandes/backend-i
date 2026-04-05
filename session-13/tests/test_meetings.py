from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def setup_function():
    """Clear DB before each test."""
    from app.api.routers import meetings

    meetings.DB.clear()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_create_meeting_ok() -> None:
    payload = {"title": "Planning", "date": "2026-03-10", "owner": "Jorge"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == "Planning"
    assert data["date"] == "2026-03-10"
    assert data["owner"] == "Jorge"
    assert "id" in data


def test_create_meeting_validation_error() -> None:
    payload = {"title": "ab", "date": "2026-03-10", "owner": "Jorge"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 422


def test_create_meeting_missing_field() -> None:
    payload = {"title": "Planning", "date": "2026-03-10"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 422


def test_get_meeting_not_found() -> None:
    r = client.get("/meetings/999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Meeting not found"


def test_get_meeting_ok() -> None:
    payload = {"title": "Test Meeting", "date": "2026-03-15", "owner": "Alice"}
    create_r = client.post("/meetings", json=payload)
    meeting_id = create_r.json()["id"]
    r = client.get(f"/meetings/{meeting_id}")
    assert r.status_code == 200
    assert r.json()["title"] == "Test Meeting"


def test_list_meetings_empty() -> None:
    r = client.get("/meetings")
    assert r.status_code == 200
    data = r.json()
    assert data["total"] == 0
    assert data["items"] == []


def test_list_meetings_with_owner_filter() -> None:
    r1 = client.post(
        "/meetings", json={"title": "Meet1", "date": "2026-03-01", "owner": "Jorge"}
    )
    assert r1.status_code == 201, f"Create failed: {r1.json()}"
    r2 = client.post(
        "/meetings", json={"title": "Meet2", "date": "2026-03-02", "owner": "Alice"}
    )
    assert r2.status_code == 201
    r3 = client.post(
        "/meetings", json={"title": "Meet3", "date": "2026-03-03", "owner": "Jorge"}
    )
    assert r3.status_code == 201
    r = client.get("/meetings?owner=Jorge")
    assert r.status_code == 200
    data = r.json()
    assert data["total"] == 2


def test_update_meeting_ok() -> None:
    create_r = client.post(
        "/meetings", json={"title": "Old", "date": "2026-03-01", "owner": "Jorge"}
    )
    meeting_id = create_r.json()["id"]
    r = client.put(
        f"/meetings/{meeting_id}",
        json={"title": "New", "date": "2026-03-02", "owner": "Jorge"},
    )
    assert r.status_code == 200
    assert r.json()["title"] == "New"
