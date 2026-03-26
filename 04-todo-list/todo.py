"""
Simple To-Do List - Project 04
------------------------------
What it does: A terminal task manager. Supports adding tasks, viewing 
the numbered list, marking tasks as done, and deleting them. 
Demonstrates the core principles of CRUD (Create, Read, Update, Delete).

Pro Hints:
- We use a List of Dictionaries `[{"name": ..., "done": True/False}]` to maintain state.
- `enumerate(list, 1)` helps securely print 1-indexed elements.
- We validate integer boundaries so deleting task 10 doesn't crash if only 2 exist.
"""

# Global state
tasks = []

def add_task(name):
    # Create
    tasks.append({"name": name, "done": False})
    print(f"Task added: '{name}'")

def show_tasks():
    # Read
    if not tasks:
        print("Your to-do list is empty.")
        return
        
    print("\n--- Your To-Do List ---")
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t['done'] else "[ ]"
        print(f"{i}. {status} {t['name']}")
    print("-----------------------\n")

def mark_done(index):
    # Update
    if 1 <= index <= len(tasks):
        tasks[index - 1]['done'] = True
        print(f"Task {index} marked as done!")
    else:
        print("Invalid task number!")

def remove_task(index):
    # Delete
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Removed task: '{removed['name']}'")
    else:
        print("Invalid task number!")

def runner():
    print("Welcome to the Simple To-Do List!")
    
    while True:
        show_tasks()
        print("Options: [A]dd  [D]one  [R]emove  [Q]uit")
        choice = input("> ").strip().lower()
        
        if choice == 'q':
            print("Exiting tool. Have a productive day!")
            break
        elif choice == 'a':
            text = input("Task description: ")
            add_task(text)
        elif choice == 'd':
            try:
                idx = int(input("Task number to mark done: "))
                mark_done(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 'r':
            try:
                idx = int(input("Task number to remove: "))
                remove_task(idx)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid option. Use A, D, R, or Q.")

if __name__ == "__main__":
    runner()
