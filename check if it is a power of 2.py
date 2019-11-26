n=int(input())
v=1
l=[]
for i in range(n+1):
	v=v+v
	l.append(v)
for j in l:
    if(j==n):
        print("yes")
        break
else:
    print("no")
