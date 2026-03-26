# 19 - Student Grade System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-3_-_File_Handling-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

A grade management system with Streamlit UI. Manages students, courses, and grades with GPA calculation.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- OOP with `Student` and `Classroom` classes
- Streamlit web interface with forms
- GPA calculation algorithm
- Pandas DataFrames for display
- Multi-module project structure

## What You Will Learn

You will learn OOP design patterns, building web UIs with Streamlit, and multi-module applications.

## Project Structure

```text
19-student-grade-system/
  README.md
  app.py
  classroom.py
  requirements.txt
  student.py
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit, pandas
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Add students with name and grade
  - View class statistics (average, highest, lowest GPA)
  - Sort and filter student records
  - Export grade reports
```
