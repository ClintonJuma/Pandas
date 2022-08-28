import pandas as pd
df = pd.read_csv("data.csv")
print(df)
print(df.info())
#Remove rows with empty cells from original
new_df = df.dropna()
print(new_df.to_string())
print(new_df.info())
#REplacing Empty values
print(df.info())
newer_df = df.fillna(130, inplace = True)
print(newer_df)