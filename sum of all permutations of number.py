from itertools import permutations
n=input()
x=permutations(n)
x=list(x)
l=[]
sum=0
for i in x:
    c=''
    for j in i:
        c=c+j
    l.append(c)
for k in l:
    sum=sum+int(k)

print(sum)
