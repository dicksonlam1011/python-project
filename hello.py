import datetime
import pandas as pd


print("Start Python Project!")
##############################################################

list=pd.to_numeric([1,2,3,4,5,6])

filter=(list>3) & (list<5)

print(list[filter])