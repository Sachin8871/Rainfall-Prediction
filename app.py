import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open("Models/xgb.pkl", "rb"))

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
    st.markdown("<br>", unsafe_allow_html=True)

    location = st.number_input("Location (encoded)", format="%.2f")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h5>Temperature of the day</h5>", unsafe_allow_html=True)
    col1, col2, cola1, cola2 = st.columns(4)
    with col1:
        minTemp = st.number_input("Min Temperature", format="%.2f")
    with col2:
        maxTemp = st.number_input("Max Temperature", format="%.2f")
    with cola1:
        temp9am = st.number_input("Temperature at 9am", format="%.2f")
    with cola2:
        temp3pm = st.number_input("Temperature at 3pm", format="%.2f")


    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        rainfall = st.number_input("Rainfall", format="%.2f")
    with col4:
        evaporation = st.number_input("Evaporation", format="%.2f")
    with col5:
        sunshine = st.number_input("Sunshine", format="%.2f")
    with col6:
        windGustSpeed = st.number_input("Wind Gust Speed", format="%.2f")


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h5>Wind and Humidity</h5>", unsafe_allow_html=True)
    
    col7, col8, col9, col10 = st.columns(4)
    with col7:
        windSpeed9am = st.number_input("Wind Speed at 9am", format="%.2f")
    with col8:
        windSpeed3pm = st.number_input("Wind Speed at 3pm", format="%.2f")
    with col9:
        humidity9am = st.number_input("Humidity at 9am", format="%.2f")
    with col10:
        humidity3pm = st.number_input("Humidity at 3pm", format="%.2f")


    col15, col16, col17 = st.columns(3)
    # Additional inputs
    with col15:
        windDir9am = st.number_input("Wind Direction at 9am (encoded)", format="%.2f")
    with col16:
        windDir3pm = st.number_input("Wind Direction at 3pm (encoded)", format="%.2f")
    with col17:
        windGustDir = st.number_input("Wind Gust Direction (encoded)", format="%.2f")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h5>Pressure and Cloud</h5>", unsafe_allow_html=True)
    col11, col12, col13, col14 = st.columns(4)
    with col11:
        pressure9am = st.number_input("Pressure at 9am", format="%.2f")
    with col12:
        pressure3pm = st.number_input("Pressure at 3pm", format="%.2f")
    with col13:
        cloud9am = st.number_input("Cloud coverage at 9am", format="%.2f")
    with col14:
        cloud3pm = st.number_input("Cloud coverage at 3pm", format="%.2f")

    st.markdown("<br>", unsafe_allow_html=True)
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
