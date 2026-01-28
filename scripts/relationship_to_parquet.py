import json
import pandas as pd

INPUT = "../data/raw/relationshipv2.json"
OUTPUT = "../data/parquet/relationship/relationship.parquet"

with open(INPUT) as f:
    data = json.load(f)

df = pd.json_normalize(data)

df.to_parquet(OUTPUT, engine="pyarrow", index=False)

print("relationship.parquet created")
