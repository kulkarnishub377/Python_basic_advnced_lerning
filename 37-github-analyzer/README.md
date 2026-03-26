# 37 - GitHub Profile Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

Analyzes a GitHub user profile using the GitHub REST API. Displays repository statistics, language usage, and profile information via Streamlit.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- GitHub REST API v3 integration
- Pagination handling for APIs
- Repository statistics aggregation
- Language usage analysis
- Streamlit charts and metrics

## What You Will Learn

You will learn how to work with paginated REST APIs, aggregate data across resources, and build analytical dashboards.

## Project Structure

```text
37-github-analyzer/
  README.md
  analyzer.py
  app.py
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
  - Enter any GitHub username
  - Profile stats: repos, followers, following
  - Language breakdown across repositories
  - Repository listing with stars and forks
```
