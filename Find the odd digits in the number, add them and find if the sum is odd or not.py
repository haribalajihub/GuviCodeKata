n=input()
c=0
for i in n:
    if(int(i)%2!=0):
        c=c+int(i)


if(c%2==0):
    print("E")
else:
    print("O")
