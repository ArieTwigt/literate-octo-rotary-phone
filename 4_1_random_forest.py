#%% open the required modules
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# %% import the german dataset
df = pd.read_csv("data/german_data_clean.csv")

# %% determine the x and y
x_columns = ['purpose', 'age_years', 'credit_amount', 
             'duration_months','job', 'present_employment_since',
             'checking_account', 'other_installment_plans', 'existing_credits']
y_column = ['response']

#%% apply the LabelEncoder
le = LabelEncoder()

for col in x_columns:
    if type(df[col][0]) == str:
        print(f"Non-numeric column found {col}. Encoding...")
        df[col] = le.fit_transform(df[col].values)


#%%
X = df[x_columns]
y = df[y_column]

#%% split in train- and test set
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.3, random_state=123)

# %% Define the model
model = RandomForestClassifier()

#%% define the parameter Grid
param_grid = {
    'n_estimators': [100, 200, 300, 400],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth': [3,4,5,6,7],
    'random_state': [123]
}

#%% Create the GridsearchCV
CV_rfc = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
CV_rfc.fit(X_train, y_train)

#%% return the best combination
best_params = CV_rfc.best_params_


# %% Train the "real model"
model_2 = RandomForestClassifier(best_params)

model_2.fit(X_train, y_train)

#%% voorspel absolute voorspellingen
predictions = model_2.predict(X_test)

# %% voorspel kansen
predictions_probabilities = model_2.predict_proba(X_test)

# %%
df_comparison = X_test
df_comparison['predictions'] = predictions
df_comparison['predictions_prob'] = predictions_probabilities[:,1]
df_comparison['actual'] = y_test

# %%
model_precision = precision_score(df_comparison['actual'], df_comparison['predictions'], pos_label=1)
model_accuracy = accuracy_score(df_comparison['actual'], df_comparison['predictions'])
# %%
print(f"Precision {model_precision}")
print(f"Accuracy {model_accuracy}")

# %% compose the confusion matrix
cf_matrix = confusion_matrix(df_comparison['actual'],
                             df_comparison['predictions'])

# %% show the raw confusion matrix
cf_matrix


#%% visualize the confusion matrix
ax = sns.heatmap(cf_matrix, annot=True, cmap="Blues", fmt="g")

# %%
ax.set_title("Confusion Matrix")
ax.set_ylabel("Actual Values")
ax.set_xlabel("Predicted Values")


# %%
plt.show()

#%% create data frame with feature importances
df_importances = pd.DataFrame()
df_importances['feature_name'] = model_2.feature_names_in_
df_importances['importance'] = model_2.feature_importances_
df_importances = df_importances.sort_values("importance", ascending=False)

# %% check the most important features
df_importances

# %%

# %%
