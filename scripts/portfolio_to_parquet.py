import json
import pandas as pd

INPUT = "../data/raw/portfolio.json"
OUTPUT = "../data/parquet/portfolio/portfolio.parquet"

with open(INPUT) as f:
    data = json.load(f)

df = pd.json_normalize(data["Portfolios"])

df.to_parquet(OUTPUT, engine="pyarrow", index=False)

print("portfolio.parquet created")