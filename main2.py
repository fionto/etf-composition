from pathlib import Path
import pandas as pd

raw_datasets_dir = Path(__file__).parent / 'data'
filename = 'Constituent_IE000YKHGYN2.xlsx'

filepath = raw_datasets_dir / filename

df = pd.read_excel(filepath, index_col=0)

currencies = (
    df.groupby("Currency")["Weighting"]
      .sum()
      .to_dict()
)

print(currencies)