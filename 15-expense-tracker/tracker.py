"""
Expense Tracker - Project 15
----------------------------
What it does: Logs daily expenses categorized by type natively. Views totals 
computed accurately by category, and filters date constraints. Visualizes 
terminal performance gracefully onto a mini chart layout. Output survives 
persistently utilizing JSON.

Pro Hints:
- We load/save our data safely from `utils.py`.
- Aggregating dict keys natively via `totals.get(category, 0) + amt` handles 
  missing assignments effortlessly without KeyErrors!
- `datetime.date.today()` is used natively rather than static strings.
"""

from datetime import date
from utils import load_data, save_data

def add_expense(amount, category, note=""):
    """
    Constructs an expense schema incorporating exactly today's date dynamically.
    """
    data = load_data()
    entry = {
        "amount": amount,
        "category": category,
        "date": str(date.today()),
        "note": note
    }
    data.append(entry)
    save_data(data)
    print(f"Logged ${amount:.2f} into '{category}'.")

def view_summary():
    """
    Parses all loaded variables grouping totals mathematically onto a dictionary.
    """
    data = load_data()
    if not data:
        print("No expenses logged.")
        return
        
    # Grouping totals gracefully
    totals = {}
    for entry in data:
        cat = entry["category"]
        amt = float(entry["amount"])
        # The core aggregation logic preventing KeyErrors
        totals[cat] = totals.get(cat, 0.0) + amt
        
    print("\n--- Expense Summary ---")
    
    # Sort mathematically descending
    sorted_totals = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    
    for category, total in sorted_totals:
        # Scale chart based on value mapping
        bar = "=" * int(total / 10) 
        print(f"{category:<15} | ${total:>8.2f} | {bar}")
    print("-----------------------\n")

if __name__ == "__main__":
    print("Expense Tracker Module Active")
    
    # Example logic simulating native operations
    # add_expense(12.50, "Food", "Snacks")
    view_summary()
