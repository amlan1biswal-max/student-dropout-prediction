import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data.csv", sep=";")

df = df[df["Target"] != "Enrolled"]

df["Target"] = df["Target"].map({
    "Graduate": 0,
    "Dropout": 1
})

selected_features = [
    "Admission grade",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)"
]

X = df[selected_features]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Accuracy:", round(accuracy*100,2), "%")

with open("model.pkl","wb") as f:
    pickle.dump(model,f)

with open("features.pkl","wb") as f:
    pickle.dump(selected_features,f)

print("Model Saved Successfully")