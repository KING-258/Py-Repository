import numpy.random
import numpy as np
t1 = (1,2)
l1 = [3,4]
a = np.array([t1,l1])
print(a)
b = np.zeros((3,3))
print(b)
c = np.arange(1,10,1).reshape(3,3)
print(c)
d = np.linspace(1,10,9)  # 1 starting 10 ending any 9 values
print(d)
e = np.random.random()  # numpy has a random module in which there is a random function
print(e)
f = np.ones((3,3)).reshape(3,3)
g = np.arange(1,10).reshape(3,3)
h = f.dot(g)
i = np.dot(g,f)
print(f)
print(g)
print(h)
print(i)
[r1, r2, r3] = np.split(g,[1,2],axis=0)  # axis = 0 means row wise and axis =1 means column wise
print(r1)
print(r2)
print(r3)
