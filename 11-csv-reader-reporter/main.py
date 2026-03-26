"""
CSV Reader & Reporter - Project 11
----------------------------------
What it does: Loads a CSV file of sales data, computes summary statistics 
per category, and prints a dynamically formatted table to the terminal.
Does not use Pandas or external libraries.

Pro Hints:
- The `csv.DictReader` automatically uses the first row of the CSV as dictionary keys!
- Dictionary comprehensions are used to quickly initialize our totals dictionary.
- We use the `with open()` context manager to ensure the file safely closes automatically.
"""

import csv
import os

def generate_report(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Could not find the file at {file_path}")
        return

    # Using 'with' is the safest way to open files in Python
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Load all rows into memory (fine for small files)
        rows = list(reader)
        
    if not rows:
        print("The CSV file is empty.")
        return

    # 1. Dictionary Comprehension: Initialize totals for every unique category to 0
    totals = {row["category"]: 0.0 for row in rows}
    
    # 2. Iterate and aggregate the float values
    for row in rows:
        try:
            val = float(row["amount"])
            totals[row["category"]] += val
        except ValueError:
            print(f"Warning: Skipping invalid amount '{row['amount']}' on row {row['id']}")

    # 3. Formatted Table Output
    print(f"\n{'Category':<20} | {'Total Sales':>15}")
    print("-" * 40)
    
    # Sort categories alphabetically before printing
    for category in sorted(totals.keys()):
        print(f"{category:<20} | ${totals[category]:>14.2f}")
    
    print("-" * 40)
    total_revenue = sum(totals.values())
    print(f"{'GRAND TOTAL':<20} | ${total_revenue:>14.2f}\n")

if __name__ == "__main__":
    print("Welcome to the CSV Data Reporter!")
    
    # Resolve absolute path relative to this script so it runs from anywhere
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_csv = os.path.join(script_dir, "data", "sample.csv")
    
    generate_report(target_csv)
