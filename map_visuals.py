#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from opencage.geocoder import OpenCageGeocode  #import libs
import json
import folium
import webbrowser
import os

# Key for the geocoder API to querey database
key = '1f8db0b1cd2c4c06a6c7d5d877a10da6'
geocoder = OpenCageGeocode(key)

def map_visualization_state(df,state): # function to visualize data on US map

    with open('gz_2010_us_outline_500k.json') as f:
        USMap = json.load(f)

# Error correction for location centering
    if state.upper() == 'GEORGIA':
        state = 'GEORGIA,USA'
    if state.upper() == 'WASHINGTON':
        state = 'WASHINGTON STATE'

# Get state lat/lon for centering
    state_lat,state_lon = state_coordinates(state)

# Initialize map
    USMap = folium.Map(location=[state_lat,state_lon], tiles='Stamen Toner', zoom_start=6)
    
# create icons for lat/lon
    winter_events = ['Avalanche','Blizzard','Cold/Wind Chill','Extreme Cold/Wind Chill','Freezing Fog','Frost/Freeze','Heavy Snow','Ice Storm','Winter Storm','Winter Weather']
    flood_events = ['Flash Flood','Flood','Heavy Rain','Lakeshore Flood']
    rain_events = ['Hail','Heavy Rain','Hurricane','Hurricane (Typhoon)', 'Tropical Depression','Tropical Storm','Waterspout','Sleet']
    heat_events = ['Drought','Dust Devil','Dust Storm','Excessive Heat','Heat','Wildfire','Volcanic Ashfall']
    lightning_events = ['Lightning','Strong Wind','Thunderstorm Wind','Tornado']

    for i,row in df.iterrows():
        if row.EVENT_TYPE in flood_events:
            colors = 'darkblue'
        elif row.EVENT_TYPE in winter_events:
            colors = 'purple'
        elif row.EVENT_TYPE in rain_events:
            colors = 'lightblue'
        elif row.EVENT_TYPE in heat_events:
            colors = 'orange'
        elif row.EVENT_TYPE in lightning_events:
            colors = 'red'
        else:
            colors = 'green'
        
        folium.CircleMarker((row.BEGIN_LAT,row.BEGIN_LON), radius=3, weight=2, color=colors, fill_color=colors, fill_opacity=.5).add_to(USMap)
        
    USMap.save('USMap.html')
    webbrowser.open('file://' + os.path.abspath('USMap.html'))
    #webbrowser.open('https://www.google.com', new=2)
    #display(USMap)

    
def state_coordinates(state): # function to query and return map coordinates

    results = geocoder.geocode(state)

    return(results[0]['geometry']['lat'],results[0]['geometry']['lng'])

