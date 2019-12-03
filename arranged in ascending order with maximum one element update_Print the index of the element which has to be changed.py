n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
        y=a.index(a[i])
        c=c+1
if(c==1):
    print(y)
else:
    print(-1)
