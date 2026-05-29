import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier


# LOAD DATASET
df = pd.read_csv(
    "data/student_data.csv",
    sep=";"
)


# CREATE DROPOUT TARGET
df["dropout"] = df["G3"].apply(
    lambda x: 1 if x < 10 else 0
)


# SELECT IMPORTANT COLUMNS ONLY
df = df[[
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2",
    "dropout"
]]


# FEATURES
X = df.drop("dropout", axis=1)


# TARGET
y = df["dropout"]


# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# RANDOM FOREST
rf_model = RandomForestClassifier()

rf_model.fit(X_train, y_train)


# PREDICTION
rf_predictions = rf_model.predict(X_test)


# ACCURACY
print("Random Forest Accuracy:")

print(
    accuracy_score(
        y_test,
        rf_predictions
    )
)


# XGBOOST
xgb_model = XGBClassifier()

xgb_model.fit(X_train, y_train)


# XGBOOST ACCURACY
xgb_predictions = xgb_model.predict(X_test)

print("XGBoost Accuracy:")

print(
    accuracy_score(
        y_test,
        xgb_predictions
    )
)


# CREATE MODELS FOLDER
os.makedirs(
    "models",
    exist_ok=True
)


# SAVE MODEL
joblib.dump(
    rf_model,
    "models/dropout_model.pkl"
)


print("Model Saved Successfully!")


# FEATURE IMPORTANCE
importance = rf_model.feature_importances_

features = X.columns


plt.figure(figsize=(8, 5))

plt.barh(features, importance)

plt.title("Feature Importance")

plt.show()