"""
Contact Book - Project 13
-------------------------
What it does: Stores, searches, updates, and deletes contacts persisted naturally 
in a JSON file. Generates a unique UUID code for every new contact.

Pro Hints:
- We abstract disk persistence entirely away into `load_contacts()` and `save_contacts()`.
- Data securely survives across multiple executions inside `data/contacts.json`.
- Uses `[c for c in contacts if search in c['name']]` as an elegant native search mechanism.
"""

import json
import uuid
import os

def get_data_filepath():
    """Ensure the target directory exists and return the filepath."""
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return os.path.join(data_dir, "contacts.json")

def load_contacts():
    path = get_data_filepath()
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        # Prevent crash if file is entirely empty
        return json.load(f) if os.path.getsize(path) > 0 else []

def save_contacts(contacts):
    path = get_data_filepath()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, email, phone):
    """Adds a new contact utilizing a universally unique identifier (UUID)."""
    contacts = load_contacts()
    new_contact = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "phone": phone
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Saved new contact: {name}")

def search_contacts(query):
    """Filters contacts natively using Python List Comprehensions."""
    contacts = load_contacts()
    query = query.lower()
    
    # We strictly match substrings natively
    matches = [c for c in contacts if query in c["name"].lower() or query in c["email"].lower()]
    
    if not matches:
        print("No contacts found.")
    else:
        for m in matches:
            print(f"- {m['name']} | {m['email']} | {m['phone']}")

def delete_contact(contact_id):
    contacts = load_contacts()
    
    # Filter the target out entirely
    updated = [c for c in contacts if c["id"] != contact_id]
    
    if len(updated) == len(contacts):
        print("Delete failed: UUID not found.")
    else:
        save_contacts(updated)
        print("Contact permanently removed.")

if __name__ == "__main__":
    print("Starting the JSON Contact Book...")
    
    # Example logic demonstrating the flow
    # add_contact("Alice Baker", "alice@test.com", "555-1234")
    print("Searching for 'Jane':")
    search_contacts("Jane")
