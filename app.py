from flask import Flask, request, jsonify
import pickle
import pandas as pd
import requests
from threading import Timer

# ----------------------------------
# Load trained model
# ----------------------------------

with open("model1.pkl", "rb") as f:
    model = pickle.load(f)

# ----------------------------------
# EXACT feature names from training
# ----------------------------------

FEATURE_NAMES = [
    'age',
    'gender',
    'membership_category',
    'days_since_last_login',
    'avg_time_spent',
    'avg_transaction_value',
    'avg_frequency_login_days',
    'points_in_wallet',
    'used_special_discount',
    'offer_application_preference',
    'past_complaint',
    'complaint_status',
    'joining_year',
    'Fiber_Optic',
    'Mobile_Data',
    'Wi-Fi'
]

EXPECTED_FEATURE_COUNT = len(FEATURE_NAMES)

# ----------------------------------
# Flask App
# ----------------------------------

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Model API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validate input
        if not data or "features" not in data:
            return jsonify({"error": "'features' field is required"}), 400

        if len(data["features"]) != EXPECTED_FEATURE_COUNT:
            return jsonify({
                "error": f"Expected {EXPECTED_FEATURE_COUNT} features, but got {len(data['features'])}"
            }), 400

        # Convert input into DataFrame with correct feature names
        input_df = pd.DataFrame(
            [data["features"]],
            columns=FEATURE_NAMES
        )

        prediction = model.predict(input_df)
        confidence = model.predict_proba(input_df).max()

        return jsonify({
            "prediction": int(prediction[0]),
            "confidence": float(confidence)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ----------------------------------
# Automatic POST Test
# ----------------------------------

def auto_test():
    url = "http://127.0.0.1:5000/predict"

    # Sample input (MATCHES FEATURE ORDER)
    sample_data = {
        "features": [
            30,     # age
            1,      # gender
            2,      # membership_category
            5,      # days_since_last_login
            45.5,   # avg_time_spent
            1200.0, # avg_transaction_value
            10,     # avg_frequency_login_days
            300,    # points_in_wallet
            1,      # used_special_discount
            0,      # offer_application_preference
            0,      # past_complaint
            0,      # complaint_status
            2021,   # joining_year
            1,      # Fiber_Optic
            0,      # Mobile_Data
            0       # Wi-Fi
        ]
    }

    try:
        response = requests.post(url, json=sample_data)
        print("Auto Test Response:", response.json())
    except Exception as e:
        print("Auto Test Failed:", e)


# ----------------------------------
# Run App
# ----------------------------------

if __name__ == "__main__":
    Timer(2, auto_test).start()
    app.run(debug=True)
