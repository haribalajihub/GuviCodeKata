n=int(input()) 
k=list(map(int,input().strip().split()))[:n]
for i in range(0,n-1,2):
    k[i],k[i+1]=k[i+1],k[i]
print(*k)
