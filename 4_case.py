#%% import required modules
import pandas as pd
import requests

#%% 
brands = ['BMW', 'AUDI', 'MERCEDES-BENZ', 'TESLA']

#%% 
df_list = []

for brand in brands:
    print(f"Importing cars for brand: {brand}")
    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"
    
    # execute the response
    response = requests.get(endpoint)

    # get the data
    data = response.json()

    # create a data frame
    data_df = pd.DataFrame(data)

    # append the data frame to the list
    df_list.append(data_df)

# %%
df_cars = pd.concat(df_list)
# %%
