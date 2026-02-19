🚗 Used Car Price Prediction API + Streamlit App

This project is an end-to-end Machine Learning system that predicts used car prices using regression models and serves predictions via an API integrated with a Streamlit frontend.

Exploratory Data Analysis notebook:
📊 

eda on used cars (2)

🔥 Features

Complete ML workflow (EDA → Training → Deployment)

Linear Regression baseline model

Hyperparameter tuning using GridSearchCV

Ridge, Lasso, ElasticNet experimentation

FastAPI prediction API

Streamlit frontend interface

Model serialization using joblib

🧠 Model Performance

Algorithm: Linear Regression

R² Score: 0.6

Tuned using cross-validation

🏗 Project Structure
project/
│
├── app/
│   ├── main.py
│   └── app.py
│
├── model/
│   ├── model.pkl
│   └── columns.pkl
│
├── data/
├── notebooks/
├── requirements.txt
└── README.md

⚙️ Installation

Clone repo

git clone <your-repo-url>
cd repo-name


Create environment

python -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt

▶️ Run API
uvicorn app.main:app --reload


Open browser:

http://127.0.0.1:8000/docs

🎯 Run Streamlit App
streamlit run app/app.py

📡 API Example Request
POST /predict


Example JSON:

{
 "year": 2015,
 "km_driven": 50000,
 "fuel": "Petrol",
 "seller_type": "Dealer",
 "transmission": "Manual"
}

🧰 Tech Stack

Python

scikit-learn

FastAPI

Streamlit

Pandas

Joblib

📈 Future Improvements

Add more features (owners, location, brand encoding)

Try ensemble models

Deploy API to cloud

Add Docker container

👨‍💻 Author

AION26