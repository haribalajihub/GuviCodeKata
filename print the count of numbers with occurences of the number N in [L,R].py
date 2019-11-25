n,k,l=input().split()
n=int(n)
k=int(k)
l=str(l)
c=0
for i in range(n,k+1):
    if l in str(i):
        c=c+1
print(c)
