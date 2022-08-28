import pandas as pd
df = pd.read_csv("data.csv")
print(df)
print(df.head(20))
print(df.tail(10))
#Info about the Data
print(df.info())