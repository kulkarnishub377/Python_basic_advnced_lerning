# 07 - Rock Paper Scissors

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Beginner](https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1_-_Absolute_Basics-blue?style=for-the-badge)

## What It Does

A classic Rock-Paper-Scissors game against the computer. The computer makes random choices and the program determines the winner with score tracking.

## Run It

```bash
python rps.py
```

## Core Concepts

- `random.choice()` for computer opponent
- Multi-condition win/lose/draw evaluation
- Score tracking across rounds
- Input validation for allowed moves
- Game loop with replay option

## What You Will Learn

You will learn how to implement game logic with multiple outcomes, use randomization for AI opponents, and maintain statistics.

## Project Structure

```text
07-rock-paper-scissors/
  README.md
  rps.py
```


## Example Output

```
Rock, Paper, Scissors!
---------------------
Enter your choice (rock/paper/scissors): rock
Computer chose: scissors
You win!

Score: You 1 - Computer 0
Play again? (y/n): n
Final Score: You 1 - Computer 0 - Draws 0
```
