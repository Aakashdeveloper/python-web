import pandas as pd
data = {'a':0.,'b':1.,'c':2.}
s = pd.Series(data)
print(s)


datab = {'Name':['John','Sarah','Tony'],
        'Age':[28,26,32]}

df= pd.DataFrame(datab,index=['rank1','rank2','rank3'])
print(df)