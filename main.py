from pathlib import Path
import pandas as pd

raw_datasets_dir = Path(__file__).parent / 'data'
filename = 'Constituent_IE000YKHGYN2.xlsx'

filepath = raw_datasets_dir / filename

df = pd.read_excel(filepath, index_col=0)

df_2 = df.head(20)

currencies = {}

for _, row in df.head(20).iterrows():
    currency = row["Currency"]
    weight = row["Weighting"]

    if currency in currencies:
        currencies[currency] += weight
    else:
        currencies[currency] = weight

print(currencies)