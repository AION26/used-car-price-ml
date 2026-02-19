from fastapi import FastAPI
import joblib
import pandas as pd 
import numpy as np  

app = FastAPI()

model = joblib.load('../model/ridge_model.pkl')
columns = joblib.load('../model/columns.pkl')

@app.get("/")
def home():
    return {"message": "Welcome to the Car Price Prediction API"}

@app.post("/predict")
def predict(data: dict):
    try:
        # Convert input data to DataFrame
        df = pd.DataFrame([data])
        df = df.reindex(columns=columns, fill_value=0)
        
        # Make prediction
        pred = model.predict(df)[0]
        price = np.exp(pred)
        
        return {"predicted_price": float(price)}
    except Exception as e:
        return {"error": str(e)}