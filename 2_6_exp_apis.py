#%% import the required libraries
import requests
import pandas as pd

# %%
brand = input("Voer kenteken in:\n").upper()
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"

#%%
resp = requests.get(endpoint)


# %%
cars_list = resp.json()

# %%
cars_df = pd.DataFrame(cars_list)

#%% convert from string to float
cars_df['catalogusprijs'] = cars_df['catalogusprijs'].astype(float)

#%% change nan to 0
cars_df['catalogusprijs'] = cars_df['catalogusprijs'].fillna(0)

#%% remove rows with 0
cars_df = cars_df.query("catalogusprijs > 0")


# %%
cars_df_grouped = (
    cars_df
    .groupby('handelsbenaming')
    .mean("catalogusprijs")
    .plot(kind='bar')
)
# %%
cars_df_grouped