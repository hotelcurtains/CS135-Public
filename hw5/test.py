import math
h = []
k = []

for i in range(0,10000):
    h.append(i)
    k.append(i)

#for i in h:
#    if ( math.floor(math.floor(i/3)/2) != math.floor (i/6) ):
#        print(i)

for i in h:
    for j in k:
        x = i + (0.5*(i+j)*(i+j+1))
        if (x != math.floor(x)):
            print(i, j)


print("done")