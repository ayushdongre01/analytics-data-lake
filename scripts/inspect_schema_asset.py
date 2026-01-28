import pandas as pd

df = pd.read_parquet("../data/parquet/asset/asset.parquet")

print(df.columns.tolist())
print(df.dtypes)