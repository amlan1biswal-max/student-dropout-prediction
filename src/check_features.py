import pickle

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

print("Total Features:", len(features))

for i, feature in enumerate(features, start=1):
    print(i, feature)