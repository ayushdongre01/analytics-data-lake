import json
import pandas as pd
import glob

files = glob.glob("../data/raw/accounts/*.json")
records = []

for file in files:
    with open(file) as f:
        records.extend(json.load(f))

df = pd.json_normalize(records)

df.to_parquet(
    "../data/parquet/account/account.parquet",
    engine="pyarrow",
    index=False
)

print("account.parquet created")
