l,u=input().split()
l=int(l)
u=int(u)
c=0
for i in range(l,u + 1):
    if i> 1:
        for j in range(2,i):
            if(i%j) == 0:
                break
        else:
            c=c+1
print(c)
