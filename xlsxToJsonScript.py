import pandas as pd
import json
data = pd.ExcelFile("German_Words_A1_A2.xlsx")
df = data.parse("Sheet1")
print(df.head())

dataset = []
_id = 0

for i in range(1, len(df)):
    dataset.append({
        "id": _id,
        "German": df["German Word"][i],
        "English": df["English Meaning"][i],
        "category": df["Category"][i],
        "score": 0})
    _id += 1

with open('dataset.json', 'w') as outfile:
    json.dump(dataset, outfile)
