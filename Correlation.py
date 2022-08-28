#corr(), calculates relationship between each column in yiur data set
import pandas as pd
df = pd.read_csv("data.csv")
print(df.corr())
#1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
#0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
#-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
#0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
