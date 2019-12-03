n=int(input())
l=[]
x=1
for i in range(2,n+1):
    x=x*2
    l.append(x)
if(n in l):
    print("yes")
else:
    print("no")
