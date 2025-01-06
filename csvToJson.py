import pandas as pd
import json

df = pd.read_csv("wordlist_1000_ash.csv", delimiter=';')
print(df.head())

_id = 0
dataset = []

print(df.columns)

for i in range(len(df)):
    dataset.append({
        "id": _id,
        "German": df["de"][i],
        "English": df["en"][i],
        "score": 0})
    _id += 1

with open('dataset.json', 'w') as outfile:
    outfile.write(json.dumps(dataset))