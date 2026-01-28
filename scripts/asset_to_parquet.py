import json
import pandas as pd

INPUT = "../data/raw/asset.json"
OUTPUT = "../data/parquet/asset/asset.parquet"

with open(INPUT) as f:
    data = json.load(f)

df = pd.json_normalize(data)

df.to_parquet(OUTPUT, engine="pyarrow", index=False)

print("asset.parquet created")