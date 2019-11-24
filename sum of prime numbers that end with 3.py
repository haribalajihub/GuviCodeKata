n=int(input())
l=[]
sum=0
for num in range(2,n+1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           l.append(num)

for j in l:
    if(j%10==3):
        sum=sum+j
print(sum)
