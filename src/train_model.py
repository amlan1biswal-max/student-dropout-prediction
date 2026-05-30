import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/student_data.csv", sep=";")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# Create target column
df["dropout"] = (df["G3"] < 10).astype(int)

# Encode categorical columns
label_encoders = {}

for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features (remove G3 and target)
X = df.drop(["dropout", "G3"], axis=1)

# Target
y = df["dropout"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model.pkl")

# Save feature names
joblib.dump(list(X.columns), "features.pkl")

print("\nModel Saved Successfully")
print("model.pkl created")
print("features.pkl created")