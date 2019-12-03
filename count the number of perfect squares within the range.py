n,k=input().split()
n=int(n)
k=int(k)
c=0
for i in range(1,k+1):
    x=i*i
    if(x>n and x<k):
        c=c+1
print(c)
