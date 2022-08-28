import pandas as pd
import numpy as np

#Create a dictonary of series
d = {"Name":pd.Series(["Tom", "James", "Ricky", "Vin", "Steve", "Smith","Jack"
                       "Lee", "David", "Gasper", "Betina", "Andres"]),
    "Age":pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
     "Rating":pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
df = pd.DataFrame(d)
print(df)
print(df.info())
print(df.loc[0])
print("The mean for Age is: ",df["Age"].mean())
print("The median for Ratig is: ",df["Rating"].median())
print("The standard deviation for Age is: ", df["Age"].std())
print(df.sum())
print(df.sum(1))
print("The minimum value in the dataframe is :", df.min())
print(df.prod())
print(df.corr())
print(df.describe())
print(df.describe(include=["object"]))#summarize string columns
print(df.describe(include="number"))#summarize numeric columns
print(df.describe(include="all"))#summarize all columns



