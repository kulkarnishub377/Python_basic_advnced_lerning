# 58 - Image Classification Web App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_Expert_Projects-blue?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)

## What It Does

A computer vision web application built with Streamlit and PyTorch. Users can upload an image (JPG, PNG), and a pre-trained Deep Learning model (ResNet-18) will analyze the image and output the top 3 most likely classifications along with their confidence scores.

## Project Structure

```text
58-image-classifier/
  app.py               # Streamlit web application & PyTorch inference
  imagenet_classes.txt # Text file containing the 1000 ImageNet categories
  requirements.txt     # Python dependencies
  README.md            # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
*(Note: This will download PyTorch, which is a large package. It may take a few minutes.)*

### 2. Run the application

```bash
streamlit run app.py
```

### 3. Open your browser
Navigate to `http://localhost:8501` and upload an image (e.g., a photo of a dog, car, or fruit) to see it classified!

## Core Concepts

- **Streamlit (`st.file_uploader`)** for handling file uploads in the browser
- **PyTorch (`torchvision.models`)** for loading a pre-trained ResNet-18 neural network
- **Image Preprocessing** using `torchvision.transforms` (resize, crop, tensor conversion, normalization)
- **Model Inference** with `torch.no_grad()` to save memory during prediction
- **Softmax Activation** to convert model logits into human-readable confidence percentages

## What You Will Learn

You will learn how to deploy a state-of-the-art Deep Learning model into a user-friendly frontend application. You'll understand the pipeline of computer vision: reading an image, applying the necessary mathematical transformations to match the model's training data, running inference, and translating raw tensors back into readable results.

## Example Output

```text
Streamlit dashboard at http://localhost:8501

Uploaded: 'golden_retriever.jpg'
Analyzing image...

Results:
1. Golden retriever (94.2%)
2. Labrador retriever (3.5%)
3. Kuvasz (0.8%)
```
