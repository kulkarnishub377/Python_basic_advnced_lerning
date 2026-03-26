"""
seed.py - Database seeder for the Capstone API.
Populates the database with sample task data for development and testing.

Usage:
    python seed.py
"""

from database import init_database, create_task, get_connection


SAMPLE_TASKS = [
    {
        "title": "Design database schema",
        "description": "Create the initial SQLite database schema with tasks table, indexes, and constraints.",
        "priority": "high",
        "assigned_to": "Alice",
    },
    {
        "title": "Implement user authentication",
        "description": "Add JWT-based authentication with login and registration endpoints.",
        "priority": "critical",
        "assigned_to": "Bob",
    },
    {
        "title": "Build dashboard frontend",
        "description": "Create a React dashboard component showing task statistics and charts.",
        "priority": "high",
        "assigned_to": "Charlie",
    },
    {
        "title": "Write unit tests for API",
        "description": "Cover all CRUD endpoints with pytest test cases. Aim for 90 percent coverage.",
        "priority": "medium",
        "assigned_to": "Alice",
    },
    {
        "title": "Set up CI/CD pipeline",
        "description": "Configure GitHub Actions to run tests, lint checks, and deploy on merge to main.",
        "priority": "medium",
        "assigned_to": "Bob",
    },
    {
        "title": "Create API documentation",
        "description": "Write comprehensive API docs with request/response examples for each endpoint.",
        "priority": "low",
        "assigned_to": "Charlie",
    },
    {
        "title": "Optimize database queries",
        "description": "Add indexes for frequently queried columns and optimize slow queries.",
        "priority": "medium",
        "assigned_to": "Alice",
    },
    {
        "title": "Implement search functionality",
        "description": "Add full-text search for tasks by title and description with ranking.",
        "priority": "high",
        "assigned_to": "Bob",
    },
    {
        "title": "Add rate limiting",
        "description": "Implement rate limiting middleware to prevent API abuse.",
        "priority": "low",
        "assigned_to": None,
    },
    {
        "title": "Deploy to production server",
        "description": "Set up the production environment with proper security, logging, and monitoring.",
        "priority": "critical",
        "assigned_to": "Charlie",
    },
]


def seed_database():
    """
    Seeds the database with sample tasks.
    Clears all existing tasks before inserting fresh data.
    """
    init_database()

    # Clear existing data
    conn = get_connection()
    try:
        conn.execute("DELETE FROM tasks")
        conn.commit()
    finally:
        conn.close()

    # Insert sample tasks
    for task_data in SAMPLE_TASKS:
        task = create_task(**task_data)
        print(f"  Created: [{task['priority'].upper()}] {task['title']}")

    print(f"\nSeeded {len(SAMPLE_TASKS)} tasks into the database.")


if __name__ == "__main__":
    print("Seeding database with sample data...\n")
    seed_database()
    print("Done.")
