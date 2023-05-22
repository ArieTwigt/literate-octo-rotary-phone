#%%
import requests
import os
import sys
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from dotenv import load_dotenv

load_dotenv()

#%% constants
OPENWEATHERMAPKEY = os.environ.get("OPENWEATHERMAPKEY")

#%%
selected_city = input("Select a city:\n")
endpoint = f"https://api.openweathermap.org/data/2.5/forecast?units=metric&q={selected_city}&appid={OPENWEATHERMAPKEY}"

# %%
response = requests.get(endpoint)

# %%
if response.status_code != 200:
    print("😞 Something went wrong")
    sys.exit()


# %% get the data
weather_data = response.json()


# %% iterate over each prediction to get the data
weather_temp_list = []
weather_feels_like_list = []
weather_rain_mm_list = []
weather_wind_speed_list = []
weather_dt_txt_list = []


for idx, value in enumerate(weather_data['list']):
    weather_temp_list.append(value['main']['temp'])
    weather_wind_speed_list.append(value['wind']['speed'])
    weather_feels_like_list.append(value['main']['feels_like'])
    try:
        weather_rain_mm_list.append(value['rain']['3h'])
    except KeyError:
        weather_rain_mm_list.append(0)
    weather_dt_txt_list.append(value['dt_txt'])

#%% create a Data Frame from the seperate lists
weather_df = pd.DataFrame({
    'date': weather_dt_txt_list,
    'temp': weather_temp_list,
    'rain_mm': weather_rain_mm_list,
    'wind_speed': weather_wind_speed_list,
    'feels_like': weather_feels_like_list
})


#%% Convert to the right data type
weather_df['date'] = pd.to_datetime(weather_df['date'])

# %% Create the visualisation
fig = go.Figure()

#%% temperature
fig.add_trace(go.Scatter(x=weather_df['date'],
                         y=weather_df['temp'],
                         name="Temperature",
                         line={
                             'color': 'blue',
                             'width': 6
                         }))

#%% feels like temperature
fig.add_trace(go.Scatter(x=weather_df['date'],
                         y=weather_df['feels_like'],
                         name="Feels like temperature",
                         line={
                             'color': 'lightblue',
                             'width': 4,
                             'dash':'dot'
                         }))

#%% wind speed
fig.add_trace(go.Bar(x=weather_df['date'], 
                     y=weather_df['wind_speed'],
                     name="Wind speed",
                     marker={
                                'color': 'gray',
                                'line': {
                                    '       width': 2
                                        },
                                'opacity': 0.6
                                }
                     ))

#%%
fig.show()
# %%
