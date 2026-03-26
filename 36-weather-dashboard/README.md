# 36 - Weather Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

Displays current weather data for any city using the Open-Meteo API with temperature, humidity, and wind speed metrics.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- Open-Meteo geocoding and weather APIs
- Multi-step API calls
- Streamlit metrics and column layouts
- Error handling for network failures
- Weather data visualization

## What You Will Learn

You will learn how to chain multiple API calls, display real-time data in dashboards, and handle API response scenarios.

## Project Structure

```text
36-weather-dashboard/
  README.md
  app.py
  requirements.txt
  weather.py
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
  - Enter any city name
  - Current temperature, humidity, wind speed
  - Weather condition description
  - Metric displays with column layout
```
