n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    if(i%2==0):
        if(a[i]<a[i+1]):
            x="yes"
        else:
            x="no"
            break
    else:
        if(a[i]>a[i+1]):
            x="yes"
        else:
            x="no"
            break
        
print(x)
