# 42 - PDF Manipulation Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)

## What It Does

PDF utilities using PyPDF2 for extracting text, merging PDFs, splitting by page range, and reading metadata.

## Run It

```bash
pip install -r requirements.txt
python pdf_tools.py
```

## Core Concepts

- `PyPDF2.PdfReader` for reading PDFs
- `PyPDF2.PdfWriter` for creating PDFs
- Text extraction from pages
- PDF merging and splitting
- Metadata extraction

## What You Will Learn

You will learn how to programmatically manipulate PDF documents and build document processing automation.

## Project Structure

```text
42-pdf-tools/
  README.md
  pdf_tools.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install PyPDF2
```


## Example Output

```
PDF Tools
---------
1. Extract Text
2. Merge PDFs
3. Split PDF
4. Get Metadata

Choice: 4
File: document.pdf
  Title: Annual Report 2024
  Author: John Smith
  Pages: 42
  Creator: Microsoft Word
```
