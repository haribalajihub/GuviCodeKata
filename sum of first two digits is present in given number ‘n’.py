n=input()
n1=n[::-1]
sum=0
p=n1[-1]
l=n1[-2]
li=p+l
for i in li:
    sum=sum+int(i)

pl=str(sum)
if(pl in n):
    print(1)
else:
    print(0)
