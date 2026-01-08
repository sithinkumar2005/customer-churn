# Machine Learning Classification Project

## Introduction
This project demonstrates a complete machine learning classification workflow implemented in Python using Jupyter Notebook. It covers data preprocessing, model training, performance evaluation, explanation of artificial intelligence logic, and saving trained models for reuse.

The project focuses on comparing a baseline classification model with an ensemble-based model to understand performance differences and practical applications.

---

## Project Objectives
- Perform data preprocessing and preparation
- Train and evaluate classification models
- Compare model performance using evaluation metrics
- Explain the working logic of machine learning models
- Save trained models for future usage

---

## Project Structure

---

## Dataset Description
- Supervised classification dataset
- Contains multiple feature variables and one target variable
- Dataset exploration and preprocessing performed using Pandas
- Missing values and data inconsistencies handled before training

---

## Methodology

### Library Usage
The project uses the following Python libraries:
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Pickle

---

### Data Preprocessing
The following preprocessing steps were applied:
- Dataset loaded into a Pandas DataFrame
- Missing values checked and handled
- Categorical data encoded into numerical format
- Dataset split into training and testing sets

---

### Model Training

#### Logistic Regression
- Linear classification algorithm
- Used as a baseline model
- Fast training and easy interpretation

#### Random Forest Classifier
- Ensemble machine learning algorithm
- Uses multiple decision trees
- Improves accuracy and reduces overfitting

---

### Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

The Random Forest model achieved superior performance compared to Logistic Regression.

---

## AI Logic Explanation
Machine learning models learn from historical data to identify patterns and relationships between features and target values. Logistic Regression creates a linear decision boundary, while Random Forest combines predictions from multiple decision trees to produce more accurate and stable results.

---

## Model Saving
The trained Random Forest model was saved using two methods for flexibility and reuse:
- Joblib
- Pickle

Saved models allow predictions to be made without retraining.

---

## Tools and Technologies
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Pickle
