import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df1 = pd.DataFrame({"HPI":[80,85,88,85],
                    "Int_rate":[2,1,2,3],"Ind_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"Ind_GDP":[50,45,45,67]},index=[2005,2006,2007,2008])


concat = pd.concat([df1,df2])

print(concat)


'''
df = pd.DataFrame({'Days':[1,2,3,4,5],'Visitors':[1000,700,1600,400,5000],'Bounce_rate':[20,30,50,60,70]})

df = df.rename(columns={"Visitors":"Users"})


df = pd.DataFrame({'Days':[1,2,3,4,5],'Visitors':[1000,700,1600,400,5000],'Bounce_rate':[20,30,50,60,70]})
df.set_index('Days',inplace=True)
df.plot()
plt.show()
#print(df)

#merge
df1 = pd.DataFrame({"Int_rate":[2,1,2,3],"Ind_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])

df2 = pd.DataFrame({"Low_tier_HPI":[80,90,70,60],"unemployment":[2,1,2,3]},index=[2001,2002,2003,2004])


joined = df1.join(df2)
#merge = pd.merge(df1,df2, on="HPI")

print(joined)






XYZ_web={'Days':[1,2,3,4,5],'Visitors':[1000,700,1600,400,5000],'Bounce_rate':[20,30,50,60,70]}

print(XYZ_web)

df = pd.DataFrame(XYZ_web)

#Slicing data
print(df.head(2))


#print(df)'''
