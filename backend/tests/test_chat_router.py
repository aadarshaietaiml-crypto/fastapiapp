import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_chat_memory_route_is_available(client):
    response = client.post(
        "/chat/memory",
        json={"message": "hi", "session_id": "s1"},
    )

    assert response.status_code == 200
    assert "reply" in response.json()
