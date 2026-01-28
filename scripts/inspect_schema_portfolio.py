import pandas as pd

df = pd.read_parquet("../data/parquet/portfolio/portfolio.parquet")

print(df.columns.tolist())
print(df.dtypes)