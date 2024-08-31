import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open("gnb.pkl", "rb"))

# Define the prediction function
def predict_weather(input_data):
    prediction = model.predict([input_data])
    return prediction[0]

# App title
st.title("Weather Prediction App")

# Input form
with st.form("prediction_form"):
    # Date input
    date = st.date_input("Select a date")
    day = float(pd.to_datetime(date).day)
    month = float(pd.to_datetime(date).month)
    year = float(pd.to_datetime(date).year)

    # Weather parameters inputs
    minTemp = st.number_input("Min Temperature", format="%.2f")
    maxTemp = st.number_input("Max Temperature", format="%.2f")
    rainfall = st.number_input("Rainfall", format="%.2f")
    evaporation = st.number_input("Evaporation", format="%.2f")
    sunshine = st.number_input("Sunshine", format="%.2f")
    windGustSpeed = st.number_input("Wind Gust Speed", format="%.2f")
    windSpeed9am = st.number_input("Wind Speed at 9am", format="%.2f")
    windSpeed3pm = st.number_input("Wind Speed at 3pm", format="%.2f")
    humidity9am = st.number_input("Humidity at 9am", format="%.2f")
    humidity3pm = st.number_input("Humidity at 3pm", format="%.2f")
    pressure9am = st.number_input("Pressure at 9am", format="%.2f")
    pressure3pm = st.number_input("Pressure at 3pm", format="%.2f")
    temp9am = st.number_input("Temperature at 9am", format="%.2f")
    temp3pm = st.number_input("Temperature at 3pm", format="%.2f")
    cloud9am = st.number_input("Cloud coverage at 9am", format="%.2f")
    cloud3pm = st.number_input("Cloud coverage at 3pm", format="%.2f")
    
    # Additional inputs
    location = st.number_input("Location (encoded)", format="%.2f")
    windDir9am = st.number_input("Wind Direction at 9am (encoded)", format="%.2f")
    windDir3pm = st.number_input("Wind Direction at 3pm (encoded)", format="%.2f")
    windGustDir = st.number_input("Wind Gust Direction (encoded)", format="%.2f")
    rainToday = st.number_input("Rain Today (0 for No, 1 for Yes)", format="%.2f")

    # Submit button
    submit = st.form_submit_button("Predict")

# Prediction
if submit:
    input_data = [
        location, minTemp, maxTemp, rainfall, evaporation, sunshine,
        windGustDir, windGustSpeed, windDir9am, windDir3pm, windSpeed9am, windSpeed3pm,
        humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm,
        temp9am, temp3pm, rainToday, year, month, day
    ]
    
    # Get prediction
    prediction = predict_weather(input_data)
    
    # Display result
    if prediction == 0:
        st.success("It's a Sunny day")
    else:
        st.success("It's a Rainy day")
