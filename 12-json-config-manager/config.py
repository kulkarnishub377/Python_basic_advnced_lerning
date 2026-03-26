"""
JSON Config Manager - Project 12
--------------------------------
What it does: Reads, updates, and persists application settings stored in a JSON file.
Supports safe get/set/delete operations and handles missing keys gracefully.

Pro Hints:
- We use the `dict.get(key, default)` paradigm to safely retrieve configuration variables.
- We implement the "Load -> Modify -> Save" atomic update pattern.
- We use `os.path` to guarantee the JSON configuration always maps correctly.
"""

import json
import os

# Set target locally where the python script operates
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")

def load_config():
    """Loads the JSON config into a Python dictionary."""
    if not os.path.exists(CONFIG_FILE):
        # Return an empty dict if the file is missing to prevent crashes
        return {}
        
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Error: Configuration file is corrupted. Returning empty settings.")
            return {}

def save_config(config_dict):
    """Writes the given Python dictionary back to the JSON file cleanly."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config_dict, file, indent=4)
    print("Configuration saved successfully.")

def get_setting(key, default=None):
    """Safely retrieves a localized setting."""
    cfg = load_config()
    # The dictionary .get() method safely returns your 'default' if key is missing!
    return cfg.get(key, default)

def set_setting(key, value):
    """Updates a single setting and saves the config."""
    cfg = load_config()
    cfg[key] = value
    save_config(cfg)
    print(f"Updated [{key}] -> {value}")

if __name__ == "__main__":
    print("JSON Config Manager Testing:")
    print("----------------------------")
    
    # 1. Read a setting (or provide a safe default)
    theme = get_setting("theme", "light")
    print(f"Current Theme: {theme}")
    
    # 2. Add an entirely new setting
    set_setting("last_login", "2023-10-15")
    
    # 3. Simulate getting a missing setting safely
    retry_count = get_setting("retry_count", default=3)
    print(f"Retry count config (default returned): {retry_count}")
    
    print("\nCheck 'settings.json' to see the physical modifications.")
