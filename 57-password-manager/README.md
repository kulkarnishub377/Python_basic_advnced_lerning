# 57 - Secure Password Manager

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_Expert_Projects-blue?style=for-the-badge)

## What It Does

A command-line password manager that securely stores credentials. It generates a strong encryption key, encrypts your passwords using Fernet (symmetric encryption), and saves them locally. You must provide the correct master key to retrieve and decrypt your passwords.

## Project Structure

```text
57-password-manager/
  manager.py           # Main CLI application
  requirements.txt     # Python dependencies
  README.md            # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate a Master Key (Do this once!)

```bash
python manager.py generate-key
```
*Save the generated key file (`secret.key`) in a safe place. If you lose it, you lose access to all your passwords.*

### 3. Add a Password

```bash
python manager.py add --service GitHub --username octocat --password supersecret123
```

### 4. Retrieve a Password

```bash
python manager.py get --service GitHub
```

## Core Concepts

- **Symmetric Encryption** using the `cryptography.fernet` module
- Key generation and secure file storage
- Command-line parsing with Python's built-in `argparse`
- Secure data serialization via JSON files
- Handling `InvalidToken` exceptions for incorrect keys

## What You Will Learn

You will learn how to apply real-world cryptography to protect sensitive user data. You'll understand the importance of encryption keys, how symmetric encryption works, and how to build a robust CLI tool for managing local secrets.

## Example Output

```text
$ python manager.py generate-key
Key generated and saved to secret.key. Keep it safe!

$ python manager.py add --service Gmail --username myemail@gmail.com --password "P@ssw0rd!"
Successfully added credentials for Gmail.

$ python manager.py get --service Gmail
Service: Gmail
Username: myemail@gmail.com
Password: P@ssw0rd!
```
