# 16 - File Organizer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-3_-_File_Handling-blue?style=for-the-badge)

## What It Does

Automatically organizes files in a directory by sorting them into subfolders based on their file extensions.

## Run It

```bash
python organizer.py
```

## Core Concepts

- `os` and `shutil` for file operations
- Extension-based file classification
- Directory creation with `os.makedirs()`
- Path manipulation with `os.path`
- Batch file processing

## What You Will Learn

You will learn filesystem operations, path manipulation, and building file automation scripts.

## Project Structure

```text
16-file-organizer/
  README.md
  config.json
  organizer.py
```


## Example Output

```
File Organizer
--------------
Scanning: /home/user/Downloads
Found 47 files to organize.

Moved 12 files to Images/
Moved 8 files to Documents/
Moved 5 files to Videos/
Moved 22 files to Other/

Done! 47 files organized into 4 folders.
```
