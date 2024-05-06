import numpy as np
import matplotlib.pyplot as plt

x = list(range(-1000,1000))
y = list(range(-1000,1000))
set = []
#second = []


for i in x:
    for j in y:
        if max(abs(i),abs(j)) == (max(abs(2),abs(0))):
            set.append((i,j))

#for i in x:
#    for j in y:
#        if max(abs(i),abs(j)) == (max(abs(3),abs(-5))):
#            second.append((i,j))

points = np.array(set)
#otherpts = np.array(second)


plt.plot([-3,3],[0,0],"k-")
plt.plot([0,0],[-3,3],"k-")
plt.plot(points[:,0],points[:,1],'ro')
#plt.plot(otherpts[:,0],otherpts[:,1],'bo')

plt.show()

