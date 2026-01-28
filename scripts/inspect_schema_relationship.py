import pandas as pd

df = pd.read_parquet("../data/parquet/relationship/relationship.parquet")

print(df.columns.tolist())
print(df.dtypes)