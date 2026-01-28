import json
import pandas as pd

INPUT = "../data/raw/portfoliogroup.json"
OUTPUT = "../data/parquet/portfolio_group/portfolio_group.parquet"

with open(INPUT) as f:
    data = json.load(f)

df = pd.json_normalize(data)

df.to_parquet(OUTPUT, engine="pyarrow", index=False)

print("portfolio_group.parquet created")
