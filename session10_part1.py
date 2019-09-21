from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np 

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.2)

plt.subplot(221)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(222)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()


'''
days =[1,2,3,4,5]

workings =[2,3,4,3,2]
eating=[2,3,4,3,2]
sleeping=[7,8,10,6,7]
playing=[13,8,7,5,8]

plt.plot([],[],color='m',label='workings',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='sleeping',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,workings,eating,sleeping,playing)
colors=['m','c','r','k']

plt.xlabel('x')
plt.ylabel('y')
plt.title('StackPlot')
plt.legend()
plt.show()

plt.show()

slices =[7,2,2,13]
activities=['Russia','India','China','USA']
cols=['c','m','r','b']

plt.pie(slices,
labels=activities,
colors=cols,
startangle=90,
shadow=True,
explode=(0,0.1,0,0),
autopct='%1.1f%%')

#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Moon Mission')
#plt.legend()
plt.show()

x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitscat',color='k',s=25,marker='o')



population_ages=[22,55,62,45,21,22,34,42,2,4,56,110,120,122,130,
111,80,54,43,42,48]

bins =[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=.8)

plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Correct")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Wrong",color='g')
plt.legend()

plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('my plot')
plt.show()

plt.plot([1,2,3],[4,5,1])
style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2=[6,9,11]
y2=[6,15,7]


plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'r',label='line two',linewidth=5)

plt.title('Compare')
plt.ylabel('Yaxis')
plt.xlabel('Xaxis')

plt.grid(True,color='k')
plt.legend()

plt.show()'''