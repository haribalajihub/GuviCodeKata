n,k=input().split()
n,k=int(n),int(k)
l=[]
for i in range(n,k+1):
    x=bin(i)[2:]
    y=x.count('1')
    for kl in range(2,y):
        if (y % kl) == 0:
            break
    else:
        l.append(y)
c=0
for ji in l:
    if(ji>1):
        c=c+1
print(c)
