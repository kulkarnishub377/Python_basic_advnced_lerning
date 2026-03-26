# Contributing Guidelines

First off, thank you for considering contributing to this repository! It's people like you that make open-source a great community.

## How Can I Contribute?

### 1. Adding a New Project

We are building a list of  Python projects. If you would like to complete one of the unassigned projects:

- Fork the repository.
- Create a new branch: `git checkout -b feature/project-name`
- Create a new directory following the numbering scheme (e.g. `05-password-generator`).
- Ensure it contains:
  - `main.py` (your code)
  - `README.md` (following the Template below)
  - `requirements.txt` (only if necessary)
- Update the Master `README.md` table to list your project.
- Create a Pull Request!

### 2. Improving Existing Projects

- Found a bug in one of the games or tools?
- Have an idea to make the code cleaner or more Pythonic?
- Submit a Pull Request with your improvements!

## Project README Template

Please ensure your project's `README.md` follows this exact format:

```markdown
# [Project Number] — [Project Name]

What it does: [Brief explanation of the project functionality]

## Run it
pip install -r requirements.txt   (omit if no dependencies needed)
python main.py

## Concepts
- [Concept 1, e.g., while loops]
- [Concept 2, e.g., random.randint()]
- [Concept 3, e.g., File I/O]

## What you'll learn
By the end, you will understand how to [briefly describe the learning outcome].
```

## Code Review Process

- Keep your code clean, well-commented, and formatted (preferably using `black` or `pep8` standards).
- Ensure your project works exactly as described in its README.
- Once submitted, your PR will be reviewed as soon as possible. We might suggest some small changes before merging.

If you have any questions, feel free to open an Issue!
