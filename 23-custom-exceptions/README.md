# 23 - Custom Exceptions Module

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)

## What It Does

Custom exception classes for a banking application with specific exceptions for insufficient funds, invalid amounts, and account errors.

## Run It

```bash
python main.py
```

## Core Concepts

- Custom exception classes inheriting from `Exception`
- Exception hierarchy design
- Context-specific error messages
- Proper `try-except` patterns
- Banking domain error handling

## What You Will Learn

You will learn how to design exception hierarchies that make error handling cleaner.

## Project Structure

```text
23-custom-exceptions/
  README.md
  bank.py
  exceptions.py
  main.py
```


## Example Output

```
Banking Exception Demo
----------------------
Depositing $500...
Balance: $500.00

Withdrawing $600...
InsufficientFundsError: Cannot withdraw $600.00. Balance is $500.00

Depositing -$50...
InvalidAmountError: Amount must be positive. Got: -50.0
```
