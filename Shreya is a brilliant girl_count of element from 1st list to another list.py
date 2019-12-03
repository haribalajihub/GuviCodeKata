n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(k):
    if(b[i] in a):
        x=a.count(b[i])
        l.append(x)
    else:
        y="Not Present"
        l.append(y)
print(*l)
