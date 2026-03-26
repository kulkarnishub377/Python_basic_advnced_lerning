import json
import os

def get_data_filepath():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return os.path.join(data_dir, "expenses.json")

def load_data():
    path = get_data_filepath()
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f) if os.path.getsize(path) > 0 else []

def save_data(data):
    path = get_data_filepath()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
