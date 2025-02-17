import streamlit as st
import pickle
import pandas as pd
from catboost import CatBoostRegressor

# Load the model
with open("deployment/model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Jewelry Price Prediction App")

# Define required columns
required_columns = ['Main_Metal', 'Target_Gender', 'Main_Gem', 'Main_Color', 'Brand_ID', 'Category']

# Input fields
main_metal = st.selectbox("Select Metal", ["Gold", "Silver", "Platinum"])
target_gender = st.selectbox("Select Target Gender", ["m", "f"])
main_gem = st.selectbox("Select Main Gem", ["Diamond", "Ruby", "Sapphire", "None"])
main_color = st.selectbox("Select Main Color", ["red", "white", "yellow"])
brand_id = st.number_input("Enter Brand ID", min_value=0, max_value=1000, step=1)
category = st.selectbox("Select Category", ["electronics.clock", "jewelry.pendant", "jewelry.bracelet",  "jewelry.brooch", "jewelry.necklace", "jewelry.ring", "jewelry.souvenir", "jewelry.stud", "jewelry.earring"])

# Convert inputs into DataFrame
input_data = pd.DataFrame([[main_metal, target_gender, main_gem, main_color, brand_id, category]],
                          columns=required_columns)

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
