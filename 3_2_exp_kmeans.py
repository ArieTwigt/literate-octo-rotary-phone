#%% import the required modules
import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator

#%% import the data set
df = pd.read_csv("data/german_data_clean.csv")

# %%
x_colums = ['age_years', 'credit_amount', 'duration_months']

df_x = df[x_colums]

# %% create the model
kmeans = KMeans(n_clusters=5)

#%% fit the model
kmeans.fit(df_x)


# %%
df_cluster_centers = pd.DataFrame(kmeans.cluster_centers_)
df_cluster_centers.columns = df_x.columns
df_cluster_centers

# %%
df_predictions = df_x
df_predictions['cluster'] = kmeans.fit_predict(df_x)
# %%
