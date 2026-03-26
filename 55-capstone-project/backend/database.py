"""
database.py - SQLite database layer for the Capstone API.
Handles table creation, CRUD operations for tasks, and
basic connection management using Python's built-in sqlite3.
"""

import sqlite3
import os
from datetime import datetime
from typing import Optional


DATABASE_PATH = os.path.join(os.path.dirname(__file__), "capstone.db")


def get_connection():
    """Create and return a database connection with row_factory enabled."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_database():
    """
    Initialize the database schema.
    Creates the tasks table if it does not already exist.
    This function is idempotent and safe to call on every startup.
    """
    conn = get_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                status TEXT DEFAULT 'pending',
                priority TEXT DEFAULT 'medium',
                assigned_to TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        conn.commit()
    finally:
        conn.close()


def create_task(title, description="", priority="medium", assigned_to=None):
    """
    Insert a new task into the database.

    Args:
        title: The task title (required).
        description: Optional detailed description.
        priority: One of 'low', 'medium', 'high', 'critical'.
        assigned_to: Optional name of the person assigned.

    Returns:
        dict: The newly created task record.
    """
    now = datetime.utcnow().isoformat()
    conn = get_connection()
    try:
        cursor = conn.execute(
            """INSERT INTO tasks (title, description, status, priority, assigned_to, created_at, updated_at)
               VALUES (?, ?, 'pending', ?, ?, ?, ?)""",
            (title, description, priority, assigned_to, now, now)
        )
        conn.commit()
        task_id = cursor.lastrowid
        return get_task_by_id(task_id)
    finally:
        conn.close()


def get_task_by_id(task_id):
    """
    Retrieve a single task by its ID.

    Args:
        task_id: Integer ID of the task.

    Returns:
        dict or None: The task record, or None if not found.
    """
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if row:
            return dict(row)
        return None
    finally:
        conn.close()


def get_all_tasks(status_filter=None, priority_filter=None, limit=100, offset=0):
    """
    Retrieve tasks with optional filtering and pagination.

    Args:
        status_filter: Optional status to filter by.
        priority_filter: Optional priority to filter by.
        limit: Maximum number of results (default 100).
        offset: Number of results to skip (for pagination).

    Returns:
        list[dict]: List of matching task records.
    """
    conn = get_connection()
    try:
        query = "SELECT * FROM tasks WHERE 1=1"
        params = []

        if status_filter:
            query += " AND status = ?"
            params.append(status_filter)
        if priority_filter:
            query += " AND priority = ?"
            params.append(priority_filter)

        query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        rows = conn.execute(query, params).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


def update_task(task_id, **fields):
    """
    Update specific fields of an existing task.

    Args:
        task_id: Integer ID of the task to update.
        **fields: Keyword arguments of fields to update.

    Returns:
        dict or None: The updated task record, or None if not found.
    """
    if not fields:
        return get_task_by_id(task_id)

    fields["updated_at"] = datetime.utcnow().isoformat()

    set_clause = ", ".join(f"{key} = ?" for key in fields)
    values = list(fields.values()) + [task_id]

    conn = get_connection()
    try:
        conn.execute(f"UPDATE tasks SET {set_clause} WHERE id = ?", values)
        conn.commit()
        return get_task_by_id(task_id)
    finally:
        conn.close()


def delete_task(task_id):
    """
    Delete a task by its ID.

    Args:
        task_id: Integer ID of the task to delete.

    Returns:
        bool: True if a row was deleted, False if not found.
    """
    conn = get_connection()
    try:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def get_dashboard_stats():
    """
    Compute aggregate statistics across all tasks.

    Returns:
        dict: Counts by status, high priority count, and completion rate.
    """
    conn = get_connection()
    try:
        total = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        pending = conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'pending'").fetchone()[0]
        in_progress = conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'in_progress'").fetchone()[0]
        completed = conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'").fetchone()[0]
        cancelled = conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'cancelled'").fetchone()[0]
        high_priority = conn.execute(
            "SELECT COUNT(*) FROM tasks WHERE priority IN ('high', 'critical')"
        ).fetchone()[0]

        completion_rate = (completed / total * 100) if total > 0 else 0.0

        return {
            "total_tasks": total,
            "pending_tasks": pending,
            "in_progress_tasks": in_progress,
            "completed_tasks": completed,
            "cancelled_tasks": cancelled,
            "high_priority_count": high_priority,
            "completion_rate": round(completion_rate, 2),
        }
    finally:
        conn.close()
