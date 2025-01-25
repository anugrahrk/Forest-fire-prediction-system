# import streamlit as st
# import joblib
# import numpy as np

# # Load the saved model
# model = joblib.load('best_forest_fire_model.joblib')

# st.title("Forest Fire Prediction")

# # Input fields for user
# temperature = st.number_input("Temperature (°C)")
# humidity = st.number_input("Humidity (%)")
# wind_speed = st.number_input("Wind Speed (km/h)")

# # Predict button
# if st.button("Predict"):
#     features = np.array([[temperature, humidity, wind_speed]])
#     prediction = model.predict(features)
#     st.write(f"Predicted Burned Area: {prediction[0]:.2f} hectares")



import streamlit as st
import joblib
import numpy as np
import datetime as dt

# Load the classification model
model = joblib.load('best_forest_fire_model.joblib')  # Make sure to train and save this model beforehand

st.title("Forest Fire Occurrence Prediction")
st.write("Predict whether a forest fire is likely to occur based on the date.")

# Input fields
date_input = st.date_input("Select a Date")
month = date_input.month
day = date_input.day
year = date_input.year

st.write(f"Selected Date: {date_input} (Month: {month}, Day: {day}, Year: {year})")

# Convert the input into model-compatible features
# Example: Generate 'season' or 'day_of_year'
season = 0  # Encode season (Winter=0, Spring=1, Summer=2, Fall=3)
if month in [12, 1, 2]:
    season = 0  # Winter
elif month in [3, 4, 5]:
    season = 1  # Spring
elif month in [6, 7, 8]:
    season = 2  # Summer
elif month in [9, 10, 11]:
    season = 3  # Fall

day_of_year = (dt.date(year, month, day) - dt.date(year, 1, 1)).days + 1

# Combine features into an array
features = np.array([[month, day, year, season, day_of_year]])

# Predict and display result
if st.button("Predict"):
    prediction = model.predict(features)  # Binary output: 0 or 1
    if prediction[0] == 1:
        st.success("A fire is likely to occur on this date.")
    else:
        st.warning("No fire is likely to occur on this date.")
