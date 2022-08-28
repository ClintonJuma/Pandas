import pandas as pd
import numpy as np
#Creating a series with random 100 numbers
s = pd.Series(np.random.randn(4), index=("a", "b", "c", "d"))
print(s)
#Axes, returns list of labels/indexes

print("The axes are: ")
print(s.axes)

#Emmpty
print("Is the object empty? ")
print(s.empty)
#ndim, returns number of dimensions of the object
print(s)
print("The dimenions of the objects are: ", s.ndim)
s = pd.Series(np.random.randn(2))
print(s)
#size of the object
print("The size of the object: ", s.size)
#Values, returs actual data in the series as an array
print("The actual data series is: ", s.values)

#Head and tail
print(s.head(2))
print(s.tail(-2))

