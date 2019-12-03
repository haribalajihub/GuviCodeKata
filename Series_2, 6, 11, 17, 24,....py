n=int(input())
x=2
c=4
l=[0,2]
for i in range(2,10000):
    x=x+c
    c=c+1
    l.append(x)
print(l[n])
