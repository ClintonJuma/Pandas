# series is like a column  in a table
import pandas as pd
a = [1, 7, 2, 3, 6]
myvar = pd.Series(a)
print(myvar)
#Labels, used to access a specified value, as an index
print(myvar[0])
#creating labels, with index arguments
b = [2, 4, 6]
var = pd.Series(b, index = ["x", "y", "z"])
print(var)
#you can access an item by referring to the label
print(var["z"])
#KEY/VALUE Obejcts as series
#keys of dictionary become labels
calories = {"day1" : 420, "day2": 380, "day3":390}
cal = pd.Series(calories)
print(cal)

