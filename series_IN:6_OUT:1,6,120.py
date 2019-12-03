import math
n=int(input())
l=[]
for i in range(1,n+1,2):
    x=math.factorial(i)
    l.append(x)

print(*l)
