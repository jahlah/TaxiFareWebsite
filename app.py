import streamlit as st
import pandas as pd
import datetime
import requests

'''
# TaxiFareModel front
'''

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 1.1. Date and time input

pickup_date = st.date_input("Date you want to travel:")
pickup_time = st.time_input("Time you want to travel:")

# 1.2. Pickup longitude
pickup_longitude = st.number_input("Longitude of your pickup-location:")

# 1.3. Pickup latitude
pickup_latitude = st.number_input("Latitude of your pickup-location:")

# 1.4. dropoff longitude
dropoff_longitude = st.number_input("Longitude of your dropoff-location:")

# 1.5. dropoff latitude
dropoff_latitude = st.number_input("Latitude of your dropoff-location:")

# 1.6. Number of passengers input
n_passenger = st.number_input("Number of passengers", min_value = 1, max_value=10 , value = int(1))

# 1.7 show pickup and dropoff on map
df = pd.DataFrame({'lon': [float(pickup_longitude), float(dropoff_longitude)],
                   'lat': [float(pickup_latitude), float(dropoff_latitude)]})

st.map(df)

# 2. Build dictionary with parameters for API

# combine date and time
pickup_datetime = str(pickup_date) + " " + str(pickup_time)
pickup_datetime = datetime.datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": n_passenger
}

# 3. Call the API
response = requests.get(url, params = params)

st.write("Your ride will probably cost", round(response.json()["fare"],2) ,"dollars")
