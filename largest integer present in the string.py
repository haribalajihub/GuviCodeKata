x = input().split()
x = [w.replace('.','') for w in x]
fl = [int(i) for i in x if i.isdigit()]
x=[]
for i in fl:
    y=i
    x.append(y)
y=list(map(int, x))
y.sort(reverse=True)

for j in y:
    print(j)
    break
