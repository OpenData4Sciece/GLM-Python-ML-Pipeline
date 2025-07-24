import pandas as pd
import joblib
from fastapi import FastAPI
import openai

app = FastAPI()

# Load model and scaler
model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Set OpenAI API key
openai.api_key = "YOUR_API_KEY"


@app.post('/predict')
def predict(data: dict):
    df = pd.DataFrame([data])
    scaled = scaler.transform(df)
    prob = model.predict_proba(scaled)[:, 1][0]

    # Call OpenAI for summarisation
    summary = summarise_prediction(prob, data)

    return {
        'churn_probability': prob,
        'explanation': summary
    }


def summarise_prediction(probability, input_data):
    prompt = f"""
You are an AI assistant. The model predicted a churn probability of {probability:.2f} for this customer with the following features:

{input_data}

Write a short, clear summary explaining this result to a business stakeholder in simple language.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response['choices'][0]['message']['content']
