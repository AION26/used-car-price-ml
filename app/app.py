import streamlit as st
import requests

st.title("Used Car Price Prediction App")

age = st.number_input("Car Age (years)")
kms = st.number_input("KM Driven")
luxury = st.selectbox("Luxury Brand", [0,1])

if st.button("Predict Price"):
    data = {
        "car_age": age,
        "kms_driven": kms,
        "is_luxury": luxury
    }

    with st.spinner("Predicting..."):
        response = requests.post("http://127.0.0.1:8000/predict", json = data)

    st.success(f"Predicted Price: ₹ {response.json()['predicted_price']:.2f}")