# 27 - Algorithm Complexity Profiler

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

Profiles and visualizes time complexity of algorithms across varying input sizes to demonstrate O(1), O(n), O(n log n), and O(n^2) behavior.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- `time.perf_counter()` for measurement
- Algorithm complexity analysis
- Multiple sorting implementations
- Streamlit chart visualization
- Performance benchmarking

## What You Will Learn

You will learn how to measure algorithm performance and understand Big-O notation through observation.

## Project Structure

```text
27-big-o-profiler/
  README.md
  algorithms.py
  app.py
  profiler.py
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
  - Select algorithms to benchmark
  - Configure input sizes (100 to 100,000)
  - Line chart showing execution time vs input size
  - Identify O(1), O(n), O(n log n), O(n^2) patterns
```
