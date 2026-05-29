import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/student_data.csv")

df = df.dropna()

le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

df.to_csv("data/cleaned_student_data.csv", index=False)

print(df.head())
