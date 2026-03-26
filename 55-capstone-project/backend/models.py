"""
models.py - Pydantic data models for the Capstone API.
Defines the schema for tasks, users, and API responses.
All models use strict type validation via Pydantic's BaseModel.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    """Enum representing the possible states of a task."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority(str, Enum):
    """Enum representing task priority levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TaskCreate(BaseModel):
    """Schema for creating a new task. Required fields only."""
    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: str = Field(default="", max_length=2000, description="Task description")
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM, description="Task priority level")
    assigned_to: Optional[str] = Field(default=None, description="Assignee name")


class TaskUpdate(BaseModel):
    """Schema for updating an existing task. All fields are optional."""
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    assigned_to: Optional[str] = None


class TaskResponse(BaseModel):
    """Schema for task data returned by the API."""
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    assigned_to: Optional[str]
    created_at: str
    updated_at: str


class DashboardStats(BaseModel):
    """Schema for the dashboard statistics endpoint."""
    total_tasks: int
    pending_tasks: int
    in_progress_tasks: int
    completed_tasks: int
    cancelled_tasks: int
    high_priority_count: int
    completion_rate: float


class HealthCheck(BaseModel):
    """Schema for the health check endpoint."""
    status: str
    version: str
    uptime_seconds: float
    database_connected: bool
