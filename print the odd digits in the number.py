n=int(input())
y=[int(d) for d in str(n)]
e=[]
for i in y:
  if(i%2!=0):
    c=i
    e.append(c)

if(len(e)==0):
    print(-1)
else:
    print(*e)
