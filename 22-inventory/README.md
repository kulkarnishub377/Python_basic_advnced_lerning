# 22 - Inventory Management System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

A product inventory system with Streamlit UI. Tracks products with SKU, name, price, and quantity with stock alerts.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- OOP with `Product` and `Inventory` classes
- JSON data persistence
- Streamlit forms for data entry
- Stock level monitoring and alerts
- SKU-based product lookup

## What You Will Learn

You will learn building business applications with OOP architecture and persistent storage.

## Project Structure

```text
22-inventory/
  README.md
  app.py
  inventory.py
  product.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit, pandas
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Add products with SKU, name, price, quantity
  - Adjust stock levels
  - Low-stock alerts for items below threshold
  - Search by SKU or product name
```
