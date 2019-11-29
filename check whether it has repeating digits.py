n=input()
l=[]
for i in n:
    if(i not in l):
        l.append(i)
if(len(n)>len(l)):
    print("yes")
else:
    print("no")
