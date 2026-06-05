import joblib

features = joblib.load("features.pkl")

print("Total Features:", len(features))
print("\nFeatures:\n")

for i, f in enumerate(features, start=1):
    print(f"{i}. {repr(f)}")