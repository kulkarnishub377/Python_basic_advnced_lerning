import argparse
import sys
import os
import shutil

def init_project(args):
    """Handles the 'init' command to scaffold a new project."""
    project_name = args.name
    
    if os.path.exists(project_name):
        print(f"[ERROR] Directory '{project_name}' already exists.")
        sys.exit(1)
        
    try:
        os.makedirs(project_name)
        
        # Create standard file structure
        with open(os.path.join(project_name, "main.py"), "w") as f:
            f.write("# Main application entry point\ndef main():\n    print('Hello World')\n\nif __name__ == '__main__':\n    main()\n")
            
        with open(os.path.join(project_name, "requirements.txt"), "w") as f:
            f.write("# Add dependencies here\n")
            
        # Create a tests directory
        os.makedirs(os.path.join(project_name, "tests"))
        with open(os.path.join(project_name, "tests", "__init__.py"), "w") as f:
            pass
            
        print(f"[SUCCESS] Scaffolding complete for project: {project_name}")
        if args.verbose:
            print(f"Created directories: ./{project_name}/, ./{project_name}/tests/")
            print(f"Created files: main.py, requirements.txt, __init__.py")
            
    except Exception as e:
        print(f"[ERROR] Failed to scaffold project: {e}")

def clean_cache(args):
    """Handles the 'clean' command to remove __pycache__ directories."""
    target_dir = args.dir
    cache_count = 0
    
    print(f"Scanning target directory '{target_dir}' for cache files...")
    for root, dirs, files in os.walk(target_dir):
        if "__pycache__" in dirs:
            cache_path = os.path.join(root, "__pycache__")
            if args.dry_run:
                print(f"[DRY-RUN] Would remove: {cache_path}")
            else:
                shutil.rmtree(cache_path)
                if args.verbose:
                    print(f"Removed: {cache_path}")
            cache_count += 1
            
    if cache_count == 0:
        print("No cache directories found!")
    else:
        action = "Would remove" if args.dry_run else "Successfully removed"
        print(f"[{'DRY-RUN' if args.dry_run else 'SUCCESS'}] {action} {cache_count} cache directories.")

def main():
    # Root parser
    parser = argparse.ArgumentParser(
        description="DevTool: A robust CLI utility for Python developers.",
        epilog="Use 'devtool <command> --help' for details on specific commands."
    )
    
    # Global arguments applied everywhere
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable highly verbose output.")
    
    # Subparsers for our modular commands
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")

    # Command 1: init
    parser_init = subparsers.add_parser("init", help="Scaffold a new empty Python project")
    parser_init.add_argument("name", type=str, help="The name of the project folder to create")
    parser_init.set_defaults(func=init_project)

    # Command 2: clean
    parser_clean = subparsers.add_parser("clean", help="Remove all __pycache__ folders recursively")
    parser_clean.add_argument("--dir", type=str, default=".", help="Target root directory (default is current folder)")
    parser_clean.add_argument("--dry-run", action="store_true", help="Simulate exactly what would be deleted without actually deleting")
    parser_clean.set_defaults(func=clean_cache)
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Route execution to the mapped function
    args.func(args)

if __name__ == "__main__":
    main()
