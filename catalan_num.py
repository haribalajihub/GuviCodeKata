import math 
n=int(input())
l=[]
for i in range(n+1):
    x=math.factorial(2*i)
    z=math.factorial(i+1)
    y=(z*math.factorial(i))
    t=int(x/y)
    l.append(t)

print(*l)

#(2n)! / ((n + 1)!
