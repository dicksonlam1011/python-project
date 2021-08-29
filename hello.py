import datetime
import pandas as pd


print("Start Python Project!")
##############################################################

list=pd.Series(["1,2,3"])
print(list.str.split(pat=","))