__author__ = 'liusir'


import pandas as pd
print(pd.__version__)

row = {'name' : "index","age" : 20,"dict" : "hunan"}
data=pd.DataFrame(row.items())
print(data)