n=int(input())
c=0
for i in range(1,n):
    for j in range(1,n):
        if(i+j==n):
            c=c+1
print(c)
