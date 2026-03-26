from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test the health endpoint returns OK."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_get_items_empty():
    """Test that items list starts empty."""
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 0
    assert data["items"] == []


def test_create_item():
    """Test creating a new item."""
    response = client.post(
        "/api/items",
        json={"name": "Laptop", "price": 999.99, "quantity": 2},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["created"]["name"] == "Laptop"
    assert data["created"]["id"] == 1


def test_get_items_after_create():
    """Test item count after creation."""
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 1


def test_get_single_item():
    """Test retrieving a single item by ID."""
    response = client.get("/api/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
