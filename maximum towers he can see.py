n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(i<=n):
        c=c+1
print(c)
