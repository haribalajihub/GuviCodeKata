n=int(input())
a=list(map(int,input().strip().split()))
s=0
l=[]
li=[]
for i in a:
    
    while(int(i)>0):
        d=int(i)%10
        i=int(i)/10
        l.append(d)

for j in range(0,n):
    if(j not in l):
         li.append(j)

if(len(li)>0):
    print(min(li))
