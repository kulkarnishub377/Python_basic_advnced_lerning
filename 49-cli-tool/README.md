# 49 - Custom CLI Tool

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)

## What It Does

A file management CLI tool built with argparse supporting file search, line counting, duplicate detection, and file comparison.

## Run It

```bash
python cli.py --help
```

## Core Concepts

- `argparse` for command-line parsing
- Subcommands for different operations
- File system walking with `os.walk()`
- File comparison and duplicates
- Rich terminal output

## What You Will Learn

You will learn how to build professional CLI tools with argument parsing, subcommands, and help text.

## Project Structure

```text
49-cli-tool/
  README.md
  cli.py
```


## Example Output

```
CLI File Tool
-------------
$ python cli.py search --pattern "*.py" --directory ./
Found 12 Python files

$ python cli.py count --file main.py
Lines: 156, Words: 423, Characters: 3,891

$ python cli.py duplicates --directory ./
Found 2 duplicate groups (3 files total)
```
