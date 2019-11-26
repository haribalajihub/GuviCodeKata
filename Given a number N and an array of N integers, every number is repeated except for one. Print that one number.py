n=int(input())
l=[int(x) for x in input().split()]
for i in set(l):
    if l.count(i)==1:
        print(i)
        break
