# Phishing Detection Using Logistic Regression

A machine learning project that uses a trained Logistic Regression model to classify input data as **Phishing** or **Not Phishing**. The project exposes predictions through a Flask API and includes a Python script for testing the API.

## Project Overview

This project demonstrates the use of a machine learning classification model for phishing detection. A saved model is loaded using Joblib, and a Flask API accepts input features in JSON format and returns a prediction.

The project files were also used in the context of exploring model deployment with Azure ML.

## Features

- Logistic Regression model for phishing classification.
- Flask API for receiving prediction requests.
- JSON-based input and output.
- Python script for testing the prediction endpoint.
- Saved model loaded using Joblib.

## Tech Stack

- Python
- Flask
- scikit-learn
- Joblib
- NumPy
- Requests
- Azure ML deployment exploration

## Project Structure

```text
phishing-detection-ml/
├── phising_lr_model.plk
├── score.py
├── test_lr_api.py
└── README.md
```

## How It Works

1. The Flask application loads the saved Logistic Regression model from `phising_lr_model.plk`.
2. The API exposes a `/predict` endpoint that accepts POST requests containing JSON data.
3. The input data is converted into a NumPy array.
4. The model predicts the class for the supplied features.
5. The API returns a JSON response containing either `phishing` or `Not Phishing`.

## API Usage

### Endpoint

```text
POST /predict
```

When running locally, the endpoint is:

```text
http://127.0.0.1:5000/predict
```

### Example Request

The model expects 30 input features per sample. The values below are illustrative placeholders, not a verified real-world phishing example.

```json
{
  "data": [
    [-1, 1, 1, 1, -1, -1, -1, -1, -1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, -1, -1, -1, 1, 1, 1, 1, -1]
  ]
}
```

### Example Response

```json
{
  "prediction": "phishing"
}
```

The actual response depends on the model's prediction.

## Running the Project Locally

### Prerequisites

- Python installed on your system.
- The files listed in the project structure.

### Install Dependencies

```bash
pip install flask joblib numpy scikit-learn requests
```

### Start the API

```bash
python score.py
```

The Flask API is configured to run locally on port `5000`.

### Test the API

In a separate terminal, run:

```bash
python test_lr_api.py
```

Ensure the Flask application is running before executing the test script.

## Limitations

- The model expects 30 input features in the format used by the training process.
- The original training code and preprocessing pipeline are not included in this repository.
- The model's accuracy and other evaluation metrics have not been documented.
- The API code does not load a separate scaler; prediction reliability therefore depends on the model's original training and preprocessing setup.
- Successful deployment to Azure has not been verified.

## Future Improvements

- Add the original model-training notebook or script.
- Document the dataset and feature meanings.
- Include verified evaluation metrics.
- Validate input data and return clearer error messages.
- Verify and document the Azure deployment process.
- Add automated tests for API predictions.

## Disclaimer

This repository is intended for educational and machine learning portfolio purposes. Predictions should not be treated as a guarantee that a URL, email, or other item is safe or malicious.

## Author

**Tayyaba Maqsood**

Machine Learning | Python | Flask | AI/ML Projects
