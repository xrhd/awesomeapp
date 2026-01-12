from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Quote Search" in response.text
    # Check for search input
    assert 'name="q"' in response.text

def test_search_empty():
    response = client.get("/search")
    assert response.status_code == 200
    # Should return some random quotes
    assert "blockquote" in response.text

def test_search_query():
    # We know "wisdom" exists
    response = client.get("/search?q=wisdom")
    assert response.status_code == 200
    assert "wisdom" in response.text.lower()
    # Check for quote card structure
    assert "bg-solarized-base2" in response.text

def test_search_no_results():
    response = client.get("/search?q=Supercalifragilisticexpialidocious_Not_A_Word")
    assert response.status_code == 200
    assert "No quotes found" in response.text
