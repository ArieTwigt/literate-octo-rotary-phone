# %%
import pandas as pd
import numpy as np

# %%
data = pd.read_csv("data/german_data_clean.csv")

# %%
data.head()
# %%
'''
- Technische samenvatting
- Statistische samenvatting
- Kolom selecteert
- Kolommen selecteert
- Functies toepassen op kolommen
- Filteren
- Groeperen/aggregeren
- Sorteren
- Pipeline

---- API's


'''

#%% technical summary 
data.info()

# %% statistical summary
data.describe()

# %% show the columns of the data frame
data.columns

# %% select a column
data['duration_months']

# %% applying the 'sum' function
data['credit_amount'].sum()

# %% describe one single column
data['credit_amount'].describe()

# %% add a new column
data['test'] = 10

# %%
data['amount_per_month'] = (data['credit_amount'] / data['duration_months']).round(2)

# %% select multiple columns
selected_columns = ['savings', 'credit_amount', 'purpose']
data[selected_columns]

# %% Filteren
data[data['credit_amount'] > 5000]

# %%
data.query("credit_amount > 5000")

# %%
data['credit_amount'] > 5000
data['age_years'] > 50

data[(data['credit_amount'] > 5000) & (data['age_years'] > 50)]



# %%
data.query("credit_amount > 5000 & age_years > 50 & purpose == 'car (new)'")

# %%
selected_columns = ['credit_amount', 'purpose']

data[selected_columns].groupby('purpose').mean('credit_amount')

# %%
selected_columns = ['credit_amount', 'purpose', 'duration_months']
data[selected_columns].groupby('purpose').agg({'duration_months': 'mean',
                                                'credit_amount': 'sum'})

# %%
'''
- ✅ Leningen voor cars ('car (new)' en 'car (used)')
- ✅ Per purpose: gemiddelde 'duration_months', totale 'credit_amount'
- ✅ Gesorteerd van hoog naar laag o.b.v. totale 'credit_amount'
- Hernoemen van kolommen

'''

selected_purposes = ['car (used)', 'car (new)', 'radio/television', 'business']


data_grouped = (
                data
                    .query("purpose == @selected_purposes")
                    .groupby('purpose')
                    .agg({'duration_months': 'mean',
                        'credit_amount': 'sum'})
                    .sort_values('credit_amount', ascending=False)
                    .rename(columns={'duration_months': 'mean_duration_months',
                                    'credit_amount': 'total_credit_amount'})
                    .query("mean_duration_months > 20")
                )


# %%
data_grouped

# %% conditional column
data['50_plus'] = np.where(data['age_years'] > 50, "yes", "no")

# %%
data['50_plus'].value_counts()

# %%
times_10 = lambda x,y: x * 10 / y

#%%
times_10(10, 2)


## Assignments

# 1.
#%% Done
df = pd.read_csv("data/german_data_clean.csv")

# 2.
#%%
df['paid_back'] = np.where(df['response'] == 0, "yes", "no")
df['paid_back'].value_counts()

# 3.
# %%
df_filtered = df.query("credit_amount >= 5000")

# 4.
# %%
df_sorted = df.sort_values(by="credit_amount", ascending=False)
df_sorted

# 5. 
#%%
selected_columns = ['purpose', 'credit_amount']
df_grouped = df[selected_columns].groupby("purpose").mean("credit_amount")
df_grouped

# 6. 
# %%
df_grouped.columns
# %%
df_grouped.reset_index()
# %%
