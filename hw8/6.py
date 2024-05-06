import math

i = list(range(1,100))
j = list(range(1,100))
k = list(range(0,100))

for a in i:
    for b in j:
        for c in k:
            print("\r", a, b, c,end="")
            if (math.gcd(a,b)!=1 and c%a==0 and c%b==0 and c%(a*b)!=0):
                f = open("6.txt", "a")
                f.write(str(a)+", "+str(b)+", "+str(c)+"\n")
                f.close()
            


print("\ndone")