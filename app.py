import streamlit as st
import pandas as pd
import datetime
import requests
#from streamlit_folium import folium_static
#import folium

'''
# TaxiFareModel front
'''

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 1.1. Date and time input
pickup_date = st.date_input("Date you want to travel:")
pickup_time = st.time_input("Time you want to travel:")

# 1.2. Pickup latitude
pickup_latitude = st.number_input("Latitude of your pickup-location:",
                                  value = 40.779896883321335,
                                  min_value = 40.0,
                                  max_value = 42.0)

# 1.3. Pickup longitude
pickup_longitude = st.number_input("Longitude of your pickup-location:" ,
                                   value = -73.96799172876831,
                                   min_value = -74.3,
                                   max_value = -72.9)


# 1.4. dropoff latitude
dropoff_latitude = st.number_input("Latitude of your dropoff-location:",
                                   value = 40.79837281456892,
                                   min_value = 40.0,
                                   max_value = 42.0)

# 1.5. dropoff longitude
dropoff_longitude = st.number_input("Longitude of your dropoff-location:",
                                    value = -73.95609679023086,
                                    min_value = -74.3,
                                    max_value = -72.9)

# 1.6. Number of passengers input
n_passenger = st.number_input("Number of passengers", min_value = 1, max_value=10 , value = int(1))

# 1.7 show pickup and dropoff on map
df = pd.DataFrame({'lon': [float(pickup_longitude), float(dropoff_longitude)],
                   'lat': [float(pickup_latitude), float(dropoff_latitude)]})

# click button
#if st.button("Show points on map"):
#    st.map(df, zoom = 10)


#center_location = [40.758896, -73.985130]
#m = folium.Map(location=center_location, control_scale=True, zoom_start=11)

#folium.Marker()

#folium_static(m)
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

# Click button to see prediction:
if st.button("predict fare"):
    st.write("Your ride will probably cost", round(response.json()["fare"],2) ,"dollars")
