import streamlit as st
import pandas as pd
import pickle

# 1. Set up page configuration
st.set_page_config(page_title="E-Commerce Delivery Delay Predictor", layout="centered")
st.title("📦 E-Commerce Delivery Delay Predictor")
st.write("Enter the shipment details below to predict if the delivery will be delayed.")

# 2. Load the saved pickle artifacts safely
@st.cache_resource
def load_artifacts():
    with open('delivery_model.pkl', 'rb') as file:
        artifacts = pickle.load(file)
    return artifacts

artifacts = load_artifacts()
preprocessor = artifacts['preprocessor']
model = artifacts['model']

# 3. Create Form Fields for User Inputs
st.subheader("📋 Shipment Details")

col1, col2 = st.columns(2)

with col1:
    delivery_partner = st.selectbox("Delivery Partner", ['delhivery', 'xpressbees', 'shadowfax', 'ecom express', 'blue dart', 'fedex', 'dhl'])
    vehicle_type = st.selectbox("Vehicle Type", ['bike', 'scooter', 'ev van', 'truck'])
    delivery_mode = st.selectbox("Delivery Mode", ['same day', 'express', 'two day'])

with col2:
    weather_condition = st.selectbox("Weather Condition", ['clear', 'cold', 'hot', 'rainy', 'foggy', 'stormy'])
    distance_km = st.number_input("Distance (in km)", min_value=1.0, max_value=1000000.0, value=150.0, step=1.0)
    package_weight_kg = st.number_input("Package Weight (in kg)", min_value=0.1, max_value=500.0, value=5.0, step=0.1)

# 4. Trigger Prediction Action
if st.button("Predict Delivery Status", type="primary"):
    # Organize input into a DataFrame matching the training feature structure
    input_df = pd.DataFrame([{
        'delivery_partner': delivery_partner,
        'vehicle_type': vehicle_type,
        'delivery_mode': delivery_mode,
        'weather_condition': weather_condition,
        'distance_km': distance_km,
        'package_weight_kg': package_weight_kg
    }])
    
    # Preprocess inputs using the loaded transformer pipeline
    input_encoded = preprocessor.transform(input_df)
    
    # Make the binary prediction
    # Using .values to handle the internal data array cleanly and avoid warnings
    prediction = model.predict(input_encoded.values if hasattr(input_encoded, 'values') else input_encoded)
    
    st.markdown("---")
    # 5. Display beautiful result interfaces based on model outcomes
    if prediction[0] == 1:
        st.error("🚨 **Prediction: This delivery is likely to be DELAYED.**")
        st.write("Consider adjusting logistical schedules or routing to account for transit bottlenecks.")
    else:
        st.success("✅ **Prediction: This delivery will arrive ON TIME.**")
        st.write("Logistics parameters appear completely clear for normal scheduled drop-off.")