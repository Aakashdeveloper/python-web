import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

country = pd.read_csv('./API_ILO_country_YU.csv',index_col=0)

df = country.head(10)

df = df.set_index(["Country Code"])

sd = df.reindex(columns=['2012','2013'])

db = sd.diff(axis=1)

db.plot(kind ='bar')
plt.show()

'''
country.to_html('unemploy.html')
'''