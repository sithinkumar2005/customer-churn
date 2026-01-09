# Machine Learning Classification Project with Flask API

## Introduction
This project implements an end-to-end machine learning classification system and deploys it using a Flask REST API. A trained Random Forest classification model is loaded and exposed through an API endpoint that accepts structured input data and returns predictions along with confidence scores.

The project demonstrates how a machine learning model can be converted into a real-world, usable API service.

---

## Project Objectives
- Train a machine learning classification model
- Save the trained model for reuse
- Deploy the model using Flask
- Accept JSON-based input data
- Return predictions with confidence values
- Automatically test the API after startup

---

## Project Structure
## Dataset Description
- Supervised classification dataset
- Customer-related behavioral and demographic features
- One target variable predicted by the model
- Data preprocessing and feature engineering performed during training

---

## Machine Learning Model
- Algorithm: Random Forest Classifier
- Model stored using Pickle (`model1.pkl`)
- Loaded at runtime for fast predictions
- Supports probability-based confidence output

---

## Flask API Description

### API Capabilities
- Loads trained model at application startup
- Validates incoming request structure
- Ensures correct number of input features
- Converts input into a Pandas DataFrame
- Returns prediction results in JSON format
- Includes automatic self-testing logic

---

## Input Features
The API expects exactly **16 features** in the following order:

1. age  
2. gender  
3. membership_category  
4. days_since_last_login  
5. avg_time_spent  
6. avg_transaction_value  
7. avg_frequency_login_days  
8. points_in_wallet  
9. used_special_discount  
10. offer_application_preference  
11. past_complaint  
12. complaint_status  
13. joining_year  
14. Fiber_Optic  
15. Mobile_Data  
16. Wi-Fi  

---


## Post/Predict
#### Request Body (JSON)

{
  "features": [
    30,
    1,
    2,
    5,
    45.5,
    1200.0,
    10,
    300,
    1,
    0,
    0,
    0,
    2021,
    1,
    0,
    0
  ]
}
#### Response
{
  "prediction": 1,
  "confidence": 0.87
}
## Application Logic
#### Model Loading
-The trained model is loaded once using Pickle
- Prevents repeated retraining
-Improves prediction speed

### Input Validation
- Checks if JSON input exists
-Ensures features field is present
-Ensures exactly 16 feature values are provided

### Prediction Process
-Input converted into a Pandas DataFrame with exact feature name.
-Prediction generated using predict()
-Confidence calculated using predict_proba()



## Automatic API Testing

The application performs an automatic test request:

-Executes shortly after server startup

-Sends a sample POST request to /predict

-Prints the response in the terminal

-Confirms the API is working correctly


## Tools and Technologies
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Pickle
- Flask
-Requests


---

## How to Run the Project
1. Open Jupyter Notebook
2. Load the file `Untitled (1).ipynb`
3. Run all cells sequentially

---

## Future Scope
- Hyperparameter tuning
- Cross-validation
- Feature importance analysis
- Model deployment using web frameworks

---
## AI Logic Explanation
The Random Forest model learns patterns from historical customer data by combining multiple decision trees. Each tree contributes to the final prediction, improving accuracy and reducing overfitting. The Flask API serves as a bridge between the trained model and external systems.  
---
## Future Enhancements
-Input schema validation

-Model versioning

-Authentication and authorization

-Cloud deployment

-Frontend integration
