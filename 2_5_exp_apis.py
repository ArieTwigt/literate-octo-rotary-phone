#%% import the required libraries
import requests
import pandas as pd

# %%
plate = input("Voer kenteken in:\n").upper()
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate}"

#%%
resp = requests.get(endpoint)

# %%
resp.status_code

# %%
cars_list = resp.json()

# %%
cars_df = pd.DataFrame(cars_list)

# %%
#selected_columns = ['kenteken', 'merk', 'handelsbenaming', 'eerste_kleur']
#cars_df = cars_df[selected_columns]

# %%
print(cars_df)

#%% export to csv
cars_df.to_csv(f"data/car_{plate}.csv", sep=";", index=False)