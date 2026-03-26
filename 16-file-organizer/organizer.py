"""
File Organizer - Project 16
---------------------------
What it does: Automatically parses a folder, categorizing specific files 
resolving distinct extensions into mapped sub-directories seamlessly (Images/, Documents/).
Config-driven mapping lives inside JSON allowing custom mapping parameters cleanly.

Pro Hints:
- We utilize `pathlib.Path`! It is incredibly robust compared to ancient `os.path`.
- We utilize `shutil.move()` natively to explicitly rewrite file headers globally.
- Features an exclusive "dry-run" mode preview mapping variables before physical execution happens!
"""

import shutil
import json
import os
from pathlib import Path

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        return json.load(f)

def organize_directory(target_folder, dry_run=True):
    config = load_config()
    target_path = Path(target_folder)
    
    if not target_path.exists() or not target_path.is_dir():
        print(f"Error: Target directory '{target_folder}' is completely invalid.")
        return

    print(f"Scanning: {target_path.absolute()}")
    print(f"Mode: {'DRY RUN (Preview)' if dry_run else 'EXECUTING (Moving)'}")
    print("-" * 50)
    
    moves_count = 0
    
    # iterdir() natively yields elements safely without parsing string representations mapping
    for item in target_path.iterdir():
        # Do not process directories! Only files natively
        if item.is_file():
            # Extract the raw .extension mapped natively safely!
            ext = item.suffix.lower()
            
            # Map the extension utilizing dict.get natively safely fallback returning "Misc"
            dest_folder_name = config.get(ext, config.get("Other", "Misc"))
            
            # Construct physical path mapped onto the target base seamlessly!
            dest_path = target_path / dest_folder_name
            dest_file = dest_path / item.name
            
            print(f"Mapped: {item.name:<25} -> {dest_folder_name}/")
            
            if not dry_run:
                # Creates physical isolated directory boundaries safely handling duplicates natively!
                dest_path.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest_file))
                
            moves_count += 1
            
    print("-" * 50)
    print(f"Processed exactly {moves_count} distinct structural file files.")

if __name__ == "__main__":
    # Test directory mapping logic:
    # E.g., organize_directory(r"C:\Users\username\Downloads", dry_run=True)
    
    # We will simulate utilizing completely native local folders 
    test_dir = os.path.dirname(__file__)
    organize_directory(test_dir, dry_run=True)
