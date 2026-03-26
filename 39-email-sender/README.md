# 39 - Programmatic Email Sender

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)

## What It Does

Sends emails programmatically using Python's `smtplib` module with support for plain text, HTML, attachments, and multiple recipients.

## Run It

```bash
python sender.py
```

## Core Concepts

- `smtplib` for SMTP protocol
- `email.mime` for multipart messages
- TLS encryption for secure connections
- Environment variables for credentials
- Attachment handling

## What You Will Learn

You will learn how SMTP email works, how to construct formatted email messages, and secure credential management.

## Project Structure

```text
39-email-sender/
  README.md
  sender.py
```


## Example Output

```
Email Sender
------------
SMTP Server: smtp.gmail.com:587
From: sender@gmail.com
To: recipient@example.com
Subject: Test Email

Connecting via TLS...
Authenticated successfully.
Email sent to recipient@example.com
```
