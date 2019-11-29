x = input().split()
x = [w.replace('.','') for w in x]
l=[]

for i in x:
	if(i.isdigit()):
	    l.append(int(i))
print(max(l))
