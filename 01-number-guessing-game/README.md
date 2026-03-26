# 01 - Number Guessing Game

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Beginner](https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1_-_Absolute_Basics-blue?style=for-the-badge)

## What It Does

The computer picks a secret random number between 1 and 100. The player guesses repeatedly and receives 'Too high' or 'Too low' hints until they guess correctly. Tracks the total number of attempts.

## Run It

```bash
python main.py
```

## Core Concepts

- Random number generation with `random.randint()`
- Infinite `while True` game loops
- Input validation with `try-except`
- Conditional branching (`if/elif/else`)
- Graceful exit with break statements

## What You Will Learn

You will learn how to build interactive command-line programs that respond to user input, validate data before processing, and maintain game state across iterations.

## Project Structure

```text
01-number-guessing-game/
  README.md
  main.py
```


## Example Output

```
Welcome to the Number Guessing Game!
I have selected a secret number between 1 and 100.
Can you guess what it is?

Enter your guess (or 'q' to quit): 50
Too high! Try again.

Enter your guess (or 'q' to quit): 25
Too low! Try again.

Enter your guess (or 'q' to quit): 37
Congratulations! You guessed the number 37 correctly!
It took you 3 attempts to win.
```
