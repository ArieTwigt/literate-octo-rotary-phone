#%% import the required modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score


#%% import the dataset
df = pd.read_csv("data/german_data_clean.csv")

# %% define the X and y
x_columns = ['age_years', 'duration_months', 'credit_amount', 'existing_credits', 'installment_rate']
y_column = ['response']

X = df[x_columns]
y = df[y_column]

#%% split the data in a train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# %% initaiate the algorithm
model = LogisticRegression()

#%% train the model
model.fit(X_train, y_train)

#%%
predictions_binary = model.predict(X_test)

# %%
predictions_probability = model.predict_proba(X_test)

# %%
df_comparison = X_test

df_comparison['prediction_binary'] = predictions_binary
df_comparison['prediction_probability'] = predictions_probability[:,1]
df_comparison['actual'] = y_test


#%% evaluate the model
accuracy_score(df_comparison['actual'], df_comparison['prediction_binary'])


# %% 
precision_score(df_comparison['actual'], df_comparison['prediction_binary'])

# %% create the confusion matrix
