# 44 - Multiprocessing Image Resizer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)

## What It Does

Resizes batches of images in parallel using multiprocessing. Leverages multiple CPU cores for significant speedup.

## Run It

```bash
pip install -r requirements.txt
python resizer.py
```

## Core Concepts

- `multiprocessing.Pool` for parallel processing
- `PIL.Image` for resizing
- CPU-bound task parallelization
- Batch file processing with glob
- Sequential vs parallel comparison

## What You Will Learn

You will learn the difference between threading and multiprocessing and how to parallelize CPU-bound tasks.

## Project Structure

```text
44-multiprocessing-resizer/
  README.md
  requirements.txt
  resizer.py
```


## Prerequisites

Install the required packages before running:

```bash
pip install Pillow
```


## Example Output

```
Multiprocessing Image Resizer
-----------------------------
Found 20 images in ./input/
Target size: 800x600
Using 4 CPU cores

Resized 20 images in 1.8 seconds
Sequential time would be: 6.4 seconds
Speedup: 3.6x

Output saved to ./output/
```
