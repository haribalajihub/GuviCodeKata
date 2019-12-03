import math
n=int(input())
a=list(map(int,input().split()))
n=math.gcd(a[0],a[1])
for i in range(1,n):
    n=math.gcd(n,a[i+1])
print(n)
