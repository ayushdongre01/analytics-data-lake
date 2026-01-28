import pandas as pd

df = pd.read_parquet("../data/parquet/account/account.parquet")

print(df.columns.tolist())
print(df.dtypes)