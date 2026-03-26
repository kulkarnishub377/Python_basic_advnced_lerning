# 35 - Real-Time Currency Converter

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

Converts currencies in real-time using the Frankfurter API with a Streamlit UI, live exchange rates, and multi-currency support.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- `requests.get()` for API calls
- JSON response parsing
- `raise_for_status()` for HTTP errors
- Streamlit selectbox and number input
- Real-time exchange rate display

## What You Will Learn

You will learn how to integrate REST APIs, parse JSON responses, handle network errors, and build dashboards for financial data.

## Project Structure

```text
35-currency-converter/
  README.md
  app.py
  converter.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit, requests
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Select source and target currencies
  - Enter amount and see real-time conversion
  - Live exchange rates from Frankfurter API
  - Supports 30+ world currencies
```
