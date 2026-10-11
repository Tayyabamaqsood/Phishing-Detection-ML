
import requests
import json

# The URL of your Flask API's predict endpoint
# If running locally, it's typically http://127.0.0.1:5000/predict
url = "http://127.0.0.1:5000/predict"

# Sample data for prediction (30 features as expected by your model)
# This example uses placeholder values. You should replace this with actual
# feature data, keeping in mind the original dataset's structure and the model's training.
# Ensure it's a list of lists, even for a single prediction.
# IMPORTANT: If your model was trained on scaled data, and you removed scaling
# from score_lr.py, the predictions here will be based on unscaled data, which might be inaccurate.

sample_features = [
    [-1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1] # Example row
]

data = {
    "data": sample_features
}

try:
    # Send the POST request
    response = requests.post(url, json=data)

    # Print the response details
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    if response.status_code == 200:
        prediction_result = response.json().get("prediction")
        print(f"Prediction: {prediction_result}")
    else:
        print(f"Error: The API returned status code {response.status_code}")
        print(f"Error Message: {response.text}")

except requests.exceptions.ConnectionError:
    print(f"Error: Could not connect to the Flask API at {url}.")
    print("Please ensure the 'score_lr.py' Flask application is running.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
