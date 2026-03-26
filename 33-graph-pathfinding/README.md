# 33 - Graph Pathfinding

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)

## What It Does

Implements graph representation with BFS and DFS pathfinding algorithms for weighted and unweighted graphs.

## Run It

```bash
python graph.py
```

## Core Concepts

- Adjacency list graph representation
- BFS using a queue
- DFS using recursion and stack
- Shortest path in unweighted graphs
- Path reconstruction

## What You Will Learn

You will learn graph theory fundamentals and how BFS and DFS explore nodes in different orders.

## Project Structure

```text
33-graph-pathfinding/
  README.md
  graph.py
  search.py
```


## Example Output

```
Graph Pathfinding Demo
----------------------
Graph: A-B, A-C, B-D, C-D, D-E

BFS (A -> E): A -> B -> D -> E (distance: 3)
DFS (A -> E): A -> B -> D -> E (distance: 3)

BFS visits: A, B, C, D, E
DFS visits: A, B, D, E, C
```
