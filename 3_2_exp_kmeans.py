#%% import the required modules
import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt

#%% import the data set
df = pd.read_csv("data/german_data_clean.csv")

# %%
x_colums = ['age_years', 'credit_amount', 'duration_months']

df_x = df[x_colums]

# %% experiment with multiple k-values

sse = []
for k in range(1, 11):
    print(f"k={k}")
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df_x)
    sse.append(kmeans.inertia_)

#%% plot for the elbow method
plt.plot(range(1,11), 
         sse)

# %% create the model
kmeans = KMeans(n_clusters=3)

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
