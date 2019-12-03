s1=input().split('#')
s2=input().split('#')
x=0
y=0
for i in s1:
    if(i.isdigit()):
        x=x+int(i)
for j in s2:
    if(j.isdigit()):
        y=y+int(j)
if(x>y):
    print(s1[0])
else:
    print(s2[0])
