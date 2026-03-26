# 52 - Machine Learning Model

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_-_Expert_Projects-blue?style=for-the-badge)

## What It Does

Trains, evaluates, and serializes a classification model using scikit-learn with data preprocessing, accuracy metrics, and model persistence.

## Run It

```bash
pip install -r requirements.txt
python train.py
```

## Core Concepts

- `scikit-learn` for model training
- Train/test splitting
- Feature scaling with `StandardScaler`
- Classification report and accuracy
- Model serialization with `joblib`

## What You Will Learn

You will learn the complete ML pipeline from data preparation to model deployment.

## Project Structure

```text
52-ml-model/
  README.md
  requirements.txt
  train.py
```


## Prerequisites

Install the required packages before running:

```bash
pip install scikit-learn, joblib
```


## Example Output

```
ML Model Training
-----------------
Loading Iris dataset (150 samples, 4 features)
Train/test split: 120/30

Training RandomForestClassifier...
Training completed in 0.42 seconds

Classification Report:
              precision  recall  f1-score
  setosa        1.00     1.00     1.00
  versicolor    0.92     0.92     0.92
  virginica     0.92     0.92     0.92

Accuracy: 0.9667
Model saved: model.joblib
```
