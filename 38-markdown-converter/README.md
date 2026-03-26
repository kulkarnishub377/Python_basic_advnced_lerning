# 38 - Markdown to HTML Converter

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

Converts Markdown text to formatted HTML. Supports headings, bold, italic, links, lists, code blocks, and blockquotes with live preview.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- Regex-based text pattern matching
- Markdown syntax parsing
- HTML generation from tokens
- Streamlit text area with live preview
- Side-by-side source and output

## What You Will Learn

You will learn text transformation with regex, how markup languages are parsed, and building live-preview editors.

## Project Structure

```text
38-markdown-converter/
  README.md
  app.py
  converter.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Enter Markdown text in the left panel
  - See rendered HTML in the right panel
  - Supports headings, bold, italic, links, lists
  - Copy converted HTML to clipboard
```
