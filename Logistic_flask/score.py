
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained Logistic Regression model
# No scaler is loaded as per user's explicit request
model = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR", "."), "phising_lr_model.plk"))

# Define the home route
@app.route("/")
def home():
  return "Logistic Regression Phishing Detection API is running"

# Define the prediction route
@app.route("/predict", methods=["POST"])
def predict():
  data = request.get_json()
  features = np.array(data["data"]) # Features are not scaled as per user request

  prediction = model.predict(features)

  if prediction[0] == 1:
    result = "phishing"
  else:
    result = "Not Phishing"
  return jsonify({
      "prediction": result
  })

# Run the application
if __name__ == '__main__':
  app.run(debug=True)