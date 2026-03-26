# 41 - Image Watermarking Tool

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

Adds text watermarks to images using Pillow with configurable text, position, opacity, font size, and a Streamlit UI.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- `PIL.Image` for image manipulation
- `PIL.ImageDraw` for text drawing
- `PIL.ImageFont` for font rendering
- Transparency and opacity control
- Streamlit file uploader

## What You Will Learn

You will learn image manipulation with Pillow, drawing operations, and building image processing tools.

## Project Structure

```text
41-image-watermark/
  README.md
  app.py
  requirements.txt
  watermark.py
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit, Pillow
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Upload an image (PNG, JPG, JPEG)
  - Enter watermark text
  - Adjust position, font size, opacity
  - Download watermarked image
```
