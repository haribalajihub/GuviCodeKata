from collections import deque
n,k=input().split()
n=int(n)
k=int(k)
a = deque(input().split())
for i in range(k):
    a.rotate()
print(*a)
