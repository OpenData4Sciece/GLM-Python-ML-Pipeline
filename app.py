import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from typing import Dict, Any
import openai
import os

app = FastAPI(title="ML Churn Prediction API", version="1.0.0")

# Load model and scaler
try:
    model = joblib.load('logistic_model.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError as e:
    print(f"Model file not found: {e}")
    print("Please ensure logistic_model.pkl and scaler.pkl exist in the project directory")
    model = None
    scaler = None

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY")

# Define input data model


class CustomerData(BaseModel):
    """Customer data for churn prediction"""
    # Add your specific features here based on your model
    # Example features (customize based on your actual model):
    age: float
    tenure: float
    monthly_charges: float
    total_charges: float
    contract_type: str
    payment_method: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "age": 45.0,
                "tenure": 24.0,
                "monthly_charges": 79.85,
                "total_charges": 1800.0,
                "contract_type": "Month-to-month",
                "payment_method": "Electronic check"
            }
        }
    )

# Response model


class PredictionResponse(BaseModel):
    churn_probability: float
    explanation: str
    input_data: Dict[str, Any]


@app.post('/predict', response_model=PredictionResponse)
def predict(data: CustomerData):
    # Check if models are loaded
    if model is None or scaler is None:
        raise HTTPException(
            status_code=503,
            detail="Model not available. Please ensure model files exist."
        )

    try:
        # Convert Pydantic model to dict for DataFrame
        input_dict = data.model_dump()
        df = pd.DataFrame([input_dict])
        scaled = scaler.transform(df)
        prob = model.predict_proba(scaled)[:, 1][0]

        # Call OpenAI for summarisation
        summary = summarise_prediction(prob, input_dict)

        return PredictionResponse(
            churn_probability=prob,
            explanation=summary,
            input_data=input_dict
        )
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Prediction error: {str(e)}")


@app.get('/health')
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None,
        "api_version": "1.0.0"
    }


def summarise_prediction(probability, input_data):
    try:
        prompt = f"""
You are an AI assistant. The model predicted a churn probability of {probability:.2f} for this customer with the following features:

{input_data}

Write a short, clear summary explaining this result to a business stakeholder in simple words.
"""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Explanation unavailable: {str(e)}"
