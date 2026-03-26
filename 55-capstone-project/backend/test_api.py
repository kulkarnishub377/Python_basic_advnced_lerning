"""
test_api.py - Unit tests for the Capstone Task Management API.
Uses pytest with FastAPI's TestClient for endpoint testing.

Usage:
    pytest test_api.py -v
"""

import pytest
from fastapi.testclient import TestClient
from main import app
from database import init_database, get_connection


@pytest.fixture(autouse=True)
def setup_database():
    """
    Fixture that runs before each test.
    Re-initializes the database and clears existing data to ensure
    each test starts from a clean state.
    """
    init_database()
    conn = get_connection()
    conn.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
    yield


@pytest.fixture
def client():
    """Provides a TestClient instance for making API requests."""
    return TestClient(app)


@pytest.fixture
def sample_task(client):
    """Creates and returns a sample task for tests that need existing data."""
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "A task created for testing purposes",
        "priority": "high",
        "assigned_to": "Tester",
    })
    return response.json()


# --- Root and Health ---

class TestHealthEndpoints:
    """Tests for the root and health check endpoints."""

    def test_root_endpoint(self, client):
        """Root endpoint should return application metadata."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "application" in data
        assert "version" in data

    def test_health_check(self, client):
        """Health endpoint should return status and database connectivity."""
        response = client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["database_connected"] is True
        assert "uptime_seconds" in data


# --- Task CRUD ---

class TestTaskCreation:
    """Tests for creating tasks."""

    def test_create_task_success(self, client):
        """Should create a task with valid data and return 201."""
        response = client.post("/api/tasks", json={
            "title": "New Task",
            "description": "Description here",
            "priority": "medium",
        })
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "New Task"
        assert data["status"] == "pending"
        assert data["id"] is not None

    def test_create_task_minimal(self, client):
        """Should create a task with only the required title field."""
        response = client.post("/api/tasks", json={"title": "Minimal"})
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Minimal"
        assert data["priority"] == "medium"

    def test_create_task_empty_title_fails(self, client):
        """Should reject a task with an empty title."""
        response = client.post("/api/tasks", json={"title": ""})
        assert response.status_code == 422


class TestTaskRetrieval:
    """Tests for retrieving tasks."""

    def test_list_empty(self, client):
        """Should return an empty list when no tasks exist."""
        response = client.get("/api/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_with_tasks(self, client, sample_task):
        """Should return all tasks when tasks exist."""
        response = client.get("/api/tasks")
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_by_id(self, client, sample_task):
        """Should return a specific task by its ID."""
        task_id = sample_task["id"]
        response = client.get(f"/api/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Test Task"

    def test_get_not_found(self, client):
        """Should return 404 for a non-existent task ID."""
        response = client.get("/api/tasks/99999")
        assert response.status_code == 404


class TestTaskUpdate:
    """Tests for updating tasks."""

    def test_update_title(self, client, sample_task):
        """Should update only the title when other fields are omitted."""
        task_id = sample_task["id"]
        response = client.put(f"/api/tasks/{task_id}", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json()["title"] == "Updated"
        assert response.json()["priority"] == "high"

    def test_update_status(self, client, sample_task):
        """Should allow changing the task status."""
        task_id = sample_task["id"]
        response = client.put(f"/api/tasks/{task_id}", json={"status": "completed"})
        assert response.status_code == 200
        assert response.json()["status"] == "completed"

    def test_update_not_found(self, client):
        """Should return 404 when updating a non-existent task."""
        response = client.put("/api/tasks/99999", json={"title": "Nope"})
        assert response.status_code == 404


class TestTaskDeletion:
    """Tests for deleting tasks."""

    def test_delete_success(self, client, sample_task):
        """Should delete an existing task and return 204."""
        task_id = sample_task["id"]
        response = client.delete(f"/api/tasks/{task_id}")
        assert response.status_code == 204

        # Verify it is gone
        response = client.get(f"/api/tasks/{task_id}")
        assert response.status_code == 404

    def test_delete_not_found(self, client):
        """Should return 404 when deleting a non-existent task."""
        response = client.delete("/api/tasks/99999")
        assert response.status_code == 404


# --- Dashboard ---

class TestDashboard:
    """Tests for the dashboard statistics endpoint."""

    def test_dashboard_empty(self, client):
        """Should return zero counts when no tasks exist."""
        response = client.get("/api/dashboard")
        assert response.status_code == 200
        data = response.json()
        assert data["total_tasks"] == 0
        assert data["completion_rate"] == 0.0

    def test_dashboard_with_data(self, client, sample_task):
        """Should reflect accurate counts after tasks are created."""
        response = client.get("/api/dashboard")
        data = response.json()
        assert data["total_tasks"] == 1
        assert data["pending_tasks"] == 1
        assert data["high_priority_count"] == 1


# --- Search ---

class TestSearch:
    """Tests for the search endpoint."""

    def test_search_by_title(self, client, sample_task):
        """Should find tasks matching the search keyword in the title."""
        response = client.get("/api/tasks/search/Test")
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_search_no_results(self, client, sample_task):
        """Should return empty list when no tasks match the keyword."""
        response = client.get("/api/tasks/search/nonexistent")
        assert response.status_code == 200
        assert response.json() == []
