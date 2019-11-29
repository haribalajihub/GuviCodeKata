n=int(input())
x=bin(n)[2:]
x1=x[::-1]
v=1
for i in x1:
    if(i=='1'):
        print(v)
        break
    v=v+1
