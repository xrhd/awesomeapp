from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "VibeRoast" in response.text

def test_rate_vibe():
    # Test valid input
    response = client.post("/rate", data={"name": "TestUser", "emoji": "🔥"})
    assert response.status_code == 200
    assert "VIBE CHECK" in response.text or "vibes" in response.text.lower()
    assert "%" in response.text

def test_rate_vibe_deterministic():
    # Same input should give same result
    response1 = client.post("/rate", data={"name": "Neo", "emoji": "💀"})
    response2 = client.post("/rate", data={"name": "Neo", "emoji": "💀"})
    
    # Extract score (simplified check)
    assert response1.text == response2.text
