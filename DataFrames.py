#DataFrame, is a two dimensional data structure, array, table with rows and columns
import pandas as pd
data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}
#named indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)


#Locate rows, gives in series
print(df.loc[["day1", "day3"]])

#Loading files in a data Frame
ds = pd.read_csv("data.csv")
print(ds)
print(ds.head())
print(ds.tail())
print(ds. to_string())#to print the entire DtaFrame
print(pd.options.display.max_rows)#checking maximum number of rows


