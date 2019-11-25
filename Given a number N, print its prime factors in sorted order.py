n=int(input())
l=[]
v=[]
sum=0
for i in range(2,n+1):
   for j in range(2,i):
       if (i % j) == 0:
           break
   else:
       l.append(i)

for k in l:
    if(n%k==0):
        v.append(k)
print(*v)
