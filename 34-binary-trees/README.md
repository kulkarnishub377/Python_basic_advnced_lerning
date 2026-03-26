# 34 - Binary Trees

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)

## What It Does

Implements a Binary Search Tree with insertion, search, deletion, and in-order, pre-order, post-order traversals.

## Run It

```bash
python tree.py
```

## Core Concepts

- BST insertion maintaining sorted order
- In-order, pre-order, post-order traversals
- Tree search with O(log n) average
- Node deletion with three cases
- Recursive tree operations

## What You Will Learn

You will learn how BSTs maintain sorted data, how traversals produce different sequences, and recursive thinking.

## Project Structure

```text
34-binary-trees/
  README.md
  traversal.py
  tree.py
```


## Example Output

```
Binary Search Tree Demo
-----------------------
Insert: 50, 30, 70, 20, 40, 60, 80

In-order:   20, 30, 40, 50, 60, 70, 80
Pre-order:  50, 30, 20, 40, 70, 60, 80
Post-order: 20, 40, 30, 60, 80, 70, 50

Search 40: Found
Search 55: Not found
Delete 30: Success
```
