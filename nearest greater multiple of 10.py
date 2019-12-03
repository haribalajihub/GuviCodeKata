n=int(input())
c=0
y=0
l=[]
for i in range(0,10000+1,10):
    l.append(i)

for j in l:
    if(n<j):
        print(j)
        break
