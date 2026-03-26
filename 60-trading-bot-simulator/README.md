# 60 - Algorithmic Trading Bot Simulator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_Expert_Projects-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## What It Does

An algorithmic trading simulator that allows users to backtest a **Moving Average Crossover** strategy on real historical stock data. Built with Streamlit, it fetches live data from Yahoo Finance, applies the trading algorithm, and visualizes the hypothetical portfolio performance over time against a simple buy-and-hold strategy.

## Project Structure

```text
60-trading-bot-simulator/
  app.py               # Streamlit application with backtesting logic
  requirements.txt     # Python dependencies
  README.md            # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the dashboard

```bash
streamlit run app.py
```

## Core Concepts

- **Financial Data Fetching** using the `yfinance` library
- **Time-Series Analysis** with `pandas` (rolling windows, shifts, cumulative returns)
- **Moving Average Crossover Strategy**: A classic quantitative trading algorithm where a short-term moving average crosses a long-term moving average to generate buy/sell signals.
- **Vectorized Backtesting**: Calculating portfolio returns across the entire dataset instantly using pandas array operations instead of slow for-loops.
- **Data Visualization** with `streamlit` line charts.

## What You Will Learn

You will learn how quantitative analysts (quants) use Python to test trading ideas before risking real money. You'll master advanced pandas operations for financial time-series data, calculate standard financial metrics (like cumulative returns), and build interactive financial dashboards.

## Example Output

```text
Streamlit dashboard at http://localhost:8501

Ticker Selected: AAPL
Date Range: 2020-01-01 to 2024-01-01
Short MA: 20 days | Long MA: 50 days

Results:
- Total Buy/Sell Trades Executed: 14
- Buy & Hold Return: +124.5%
- Strategy Return: +142.1%

[Interactive Chart showing Stock Price, Moving Averages, and Buy/Sell Markers]
[Interactive Chart showing Portfolio Value Growth]
```
