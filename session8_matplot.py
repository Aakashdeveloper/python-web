import matplotlib.pyplot as plt

'''x= [6,3,8]
y=[3,17,5]
plt.plot(x,y)
plt.title('MatPlot Graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()'''

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,30],label="Audi",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,60,20,40,30],label="Merc",width=.5,color='r')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('information')
plt.show()