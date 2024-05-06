z = list(range(0,11))
for i in z:
    for j in z:
        if i != j and (i-j)%3 == 0:
            print("(",i,",",j,")")