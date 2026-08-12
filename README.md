# Used Car Price Prediction ML System

End-to-end machine learning project predicting used car prices using advanced modeling techniques.

## Key Features
- Comprehensive EDA with visual analysis
- Multiple regression models with hyperparameter tuning
- Real-time prediction API with Streamlit frontend

## Data Insights (from EDA)
1. **Price Distribution**: Right-skewed distribution (£110k-£195k range)
2. **Key Factors**:
   - Strong price correlation with age (newer cars cost 26% more)
   - Km-driven impact varies by brand (luxury cars depreciate slower)
3. **Model Performance**:
   - Ridge Regression: R²=0.60, RMSE=£224
   - Gradient Boosting outperforms with R²=0.58
4. **Luxury Premium**: BMW, Mercedes, and Porsche models maintain 60%+ of their value

## System Architecture
- **Backend**: FastAPI service with joblib model loading
- **Frontend**: Streamlit dashboard with live predictions
- **Pipeline**: Full data preprocessing (currency conversion, unit standardization)

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run API: `uvicorn api.main:app --reload`
3. Access frontend: `streamlit run app/app.py`

![Price vs Age](app/screenshots/1771523169424.jpg)
![Input Form](app/screenshots/1771523169319.jpg)
![Prediction Result](app/screenshots/1771523169362.jpg)

This system uses advanced feature engineering including:
- Age in years calculation
- Km-per-year metric
- Luxury brand classification
- Log price transformation for scale compression