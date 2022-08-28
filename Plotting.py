import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
df.plot()


#Scatter plot

df.plot(kind = "scatter", x = "Duration", y = "Calories")
plt.show()

#Histogram
df["Duration"].plot(kind = "hist")
print(df)