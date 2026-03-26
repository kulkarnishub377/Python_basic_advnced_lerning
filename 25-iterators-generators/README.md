# 25 - Iterators and Generators

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)

## What It Does

Demonstrates Python iterator protocol and generator functions with custom range iterators, Fibonacci generators, and infinite sequences.

## Run It

```bash
python main.py
```

## Core Concepts

- Implementing `__iter__()` and `__next__()`
- The `yield` keyword and generators
- Lazy evaluation for memory efficiency
- Custom iterator classes
- Infinite sequence generation

## What You Will Learn

You will learn the Python iterator protocol, how generators provide lazy evaluation, and when to use generators vs lists.

## Project Structure

```text
25-iterators-generators/
  README.md
  generators.py
  iterators.py
  main.py
```


## Example Output

```
Iterator and Generator Demo
---------------------------
Countdown: 5, 4, 3, 2, 1

Fibonacci (first 10): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Custom Range (0 to 10, step 2): 0, 2, 4, 6, 8

Infinite counter (first 5): 0, 1, 2, 3, 4
```
