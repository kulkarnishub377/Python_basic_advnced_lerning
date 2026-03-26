"""
routes.py - API route handlers for the Capstone project.
Contains all endpoint logic for task CRUD, dashboard stats,
health checks, and search functionality.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from models import (
    TaskCreate, TaskUpdate, TaskResponse,
    DashboardStats, HealthCheck
)
import database as db
import time


# Track application start time for uptime reporting
APP_START_TIME = time.time()

# Create the API router with a /api prefix for all endpoints
router = APIRouter(prefix="/api", tags=["tasks"])


# --- Health Check ---

@router.get("/health", response_model=HealthCheck)
def health_check():
    """
    Returns the current health status of the API.
    Used by monitoring tools and frontend status indicators.
    """
    uptime = time.time() - APP_START_TIME
    try:
        db.get_connection().close()
        db_ok = True
    except Exception:
        db_ok = False

    return HealthCheck(
        status="healthy" if db_ok else "degraded",
        version="1.0.0",
        uptime_seconds=round(uptime, 2),
        database_connected=db_ok,
    )


# --- Dashboard Stats ---

@router.get("/dashboard", response_model=DashboardStats)
def get_dashboard():
    """
    Returns aggregate statistics for the dashboard display.
    Includes task counts by status, priority breakdown, and completion rate.
    """
    stats = db.get_dashboard_stats()
    return DashboardStats(**stats)


# --- Task CRUD ---

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    """
    Create a new task with the given details.
    Automatically sets status to 'pending' and timestamps to now.
    """
    result = db.create_task(
        title=task.title,
        description=task.description,
        priority=task.priority.value,
        assigned_to=task.assigned_to,
    )
    return TaskResponse(**result)


@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(
    status: Optional[str] = Query(default=None, description="Filter by status"),
    priority: Optional[str] = Query(default=None, description="Filter by priority"),
    limit: int = Query(default=50, ge=1, le=200, description="Results per page"),
    offset: int = Query(default=0, ge=0, description="Number of results to skip"),
):
    """
    List all tasks with optional filtering and pagination.
    Supports filtering by status and priority, with configurable page size.
    """
    tasks = db.get_all_tasks(
        status_filter=status,
        priority_filter=priority,
        limit=limit,
        offset=offset,
    )
    return [TaskResponse(**t) for t in tasks]


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """Retrieve a single task by its unique ID."""
    task = db.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return TaskResponse(**task)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updates: TaskUpdate):
    """
    Update an existing task. Only provided fields are modified.
    Omitted fields retain their current values.
    """
    existing = db.get_task_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")

    update_data = {}
    if updates.title is not None:
        update_data["title"] = updates.title
    if updates.description is not None:
        update_data["description"] = updates.description
    if updates.status is not None:
        update_data["status"] = updates.status.value
    if updates.priority is not None:
        update_data["priority"] = updates.priority.value
    if updates.assigned_to is not None:
        update_data["assigned_to"] = updates.assigned_to

    result = db.update_task(task_id, **update_data)
    return TaskResponse(**result)


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """
    Permanently delete a task by its ID.
    Returns 204 No Content on success, 404 if the task does not exist.
    """
    deleted = db.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")


# --- Search ---

@router.get("/tasks/search/{keyword}", response_model=list[TaskResponse])
def search_tasks(keyword: str):
    """
    Search tasks by keyword in title or description.
    Uses case-insensitive SQL LIKE matching.
    """
    conn = db.get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM tasks WHERE title LIKE ? OR description LIKE ? ORDER BY created_at DESC",
            (f"%{keyword}%", f"%{keyword}%"),
        ).fetchall()
        return [TaskResponse(**dict(row)) for row in rows]
    finally:
        conn.close()
