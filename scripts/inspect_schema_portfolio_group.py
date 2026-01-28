import pandas as pd

df = pd.read_parquet("../data/parquet/portfolio_group/portfolio_group.parquet")

print(df.columns.tolist())
print(df.dtypes)