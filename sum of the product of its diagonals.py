n=int(input())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)

p=1
q=1
for i in range(0,n):
    for j in range(0,n):
        if (i==j):
            p=p*a[i][j] 
        if ((i+j) == (n-1)): 
            q=q*a[i][j]

x=p+q
print(x)
