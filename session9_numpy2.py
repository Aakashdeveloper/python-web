import numpy as np 

a = np.array([(1,2,3,4),(6,7,8,9),(11,12,13,14)])

#print(a[0:2,3])

b = np.linspace(1,5,8)
#print(b)

c = np.array([1,2,3])
#print(c.min())
#print(c.sum())
d = np.array([(1,2,3),(6,7,8)])
e = np.array([(1,2,3),(6,7,8)])
#print(d.sum(axis=1))
#print(np.sqrt(d))
#print(np.std(d))
#print(d-e)
#print(np.vstack((d,e)))
#print(np.hstack((d,e)))
print(d.ravel())

