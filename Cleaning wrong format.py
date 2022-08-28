import pandas as pd
df = pd.read_csv("wrong.csv")
print(df)
#you can either remove rows or convert cells in the column into same format
#converting all cells in Dates column into dates using to_datetime () method
print(df.info())

#Wrong data
df.loc[7, "Duration"] = 45
print(df.to_string())

#REmoving rows
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)

#Removing dupliactes
print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df.to_string())