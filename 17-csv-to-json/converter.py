"""
CSV to JSON Converter - Project 17
----------------------------------
What it does: An executable command-line tool explicitly converting any purely mapped `CSV` file 
straight onto well-structured schema `JSON`. Inherently supports dynamic variable-type inference 
(integers, booleans, nulls explicitly) automatically interpreting strings cleanly dynamically.

Pro Hints:
- We rely absolutely onto the internal library `argparse` structure safely executing mapping dynamically.
- `infer_type(val)` prevents dumping completely unformatted "30" instead explicitly generating integer `30` dynamically safely parsing output cleanly natively.
"""

import argparse
import csv
import json
import os

def infer_type(value):
    """
    Takes a string and explicitly infers what boolean/number variable format 
    it functionally mimics structurally seamlessly.
    """
    value = value.strip()
    
    if value == "":
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
        
    # Attempt parsing natively onto explicit integers safely limits
    try:
        if '.' in value:
            return float(value)
        return int(value)
    except ValueError:
        return value # Fallback explicitly returning raw strings uniformly

def convert_csv_json(input_path, indent=2):
    if not os.path.exists(input_path):
        print(f"Error: Valid target {input_path} natively inaccessible constraints.")
        return
        
    out_path = input_path.replace(".csv", ".json")
    
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            # We construct explicitly type-inferred dictionary variables mapping safely
            inferred_row = {k: infer_type(v) for k, v in row.items()}
            data.append(inferred_row)
            
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
        
    print(f"Success! Native format conversion completed dynamically mapped -> {out_path}")

if __name__ == "__main__":
    # We map argparse directly structuring native cli executions safely seamlessly
    parser = argparse.ArgumentParser(description="Convert explicit CSV data safely natively onto pure JSON logic formats.")
    # In a real environment, you'd use parser.add_argument("input")
    # For demo purposes, we will default mapping the internal string directly:
    default_csv = os.path.join(os.path.dirname(__file__), "sample.csv")
    
    parser.add_argument("--input", default=default_csv, help="Path resolving target specifically.")
    parser.add_argument("--indent", type=int, default=4, help="Format indentation count parameters explicitly.")
    
    args = parser.parse_args()
    
    convert_csv_json(args.input, args.indent)
