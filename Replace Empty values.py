import pandas as pd
df = pd.read_csv("data.csv")
print(df)
df.fillna(130, inplace = True)
print(df.info())

#Replace using mean, median and mode
ds = pd.read_csv("data.csv")
print(ds.info())
x = ds["Calories"]. mean()
y = ds["Maxpulse"]. mode()
z = ds["Duration"]. median()
print(x)
print(y)
print(z)
ds["Calories"].fillna(x, inplace = True)
print(ds.info())