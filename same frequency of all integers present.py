from collections import Counter
a=input()
c=Counter(a)
y=c.values()
u=list(y)
for i in range(len(u)-1):
    if(u[i]==u[i+1]):
        x=1
    else:
        x=0
        break
print(x)
