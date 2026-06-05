import pandas as pd

df = pd.read_csv("data.csv", sep=";")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nTarget Values:")
print(df["Target"].value_counts())