import sqlite3
import os

DB_NAME = "app_database.db"
MIGRATIONS_DIR = "migrations"

def ensure_migrations_table(conn):
    """
    Creates the 'schema_migrations' table if it doesn't exist.
    This tracks which migrations have already been applied.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schema_migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            version TEXT UNIQUE NOT NULL,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

def get_applied_migrations(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT version FROM schema_migrations")
    return {row[0] for row in cursor.fetchall()}

def run_migrations():
    if not os.path.exists(MIGRATIONS_DIR):
        os.makedirs(MIGRATIONS_DIR)
        print(f"Created {MIGRATIONS_DIR}/ folder. Please add .sql migration files.")
        
        # Create an initial dummy migration for demonstration
        with open(os.path.join(MIGRATIONS_DIR, "001_initial_schema.sql"), "w") as f:
            f.write("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL);\n")
        with open(os.path.join(MIGRATIONS_DIR, "002_add_user_status.sql"), "w") as f:
            f.write("ALTER TABLE users ADD COLUMN status TEXT DEFAULT 'active';\n")
            
    conn = sqlite3.connect(DB_NAME)
    try:
        ensure_migrations_table(conn)
        applied = get_applied_migrations(conn)
        
        # Get all .sql files in the migrations directory, sorted alphabetically
        migration_files = sorted([f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql")])
        
        if not migration_files:
            print("No migration files found.")
            return

        for filename in migration_files:
            if filename not in applied:
                print(f"Applying migration: {filename}...")
                filepath = os.path.join(MIGRATIONS_DIR, filename)
                
                with open(filepath, 'r') as f:
                    sql_script = f.read()
                    
                cursor = conn.cursor()
                # Use executescript to run multiple statements
                cursor.executescript(sql_script)
                
                # Mark as applied
                cursor.execute("INSERT INTO schema_migrations (version) VALUES (?)", (filename,))
                conn.commit()
                print(f"[SUCCESS] {filename} applied.")
            else:
                print(f"[SKIP] {filename} already applied.")
                
        print("Database is up to date!")
        
    except sqlite3.Error as e:
        print(f"[ERROR] Database migration failed: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    print("Database Migration Tool")
    print("-" * 25)
    run_migrations()
