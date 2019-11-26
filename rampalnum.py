num=int(input())
x=abs(num)%100
sum=0
temp=x
n=num*-1
vl=num*-1
while temp >= 10:
    temp= temp // 10
vl=vl%10
sd=n+vl 
if(num<0):
    if(sd%4==0):
        print("Yes")
    else:
        print("No")
elif(num>0):
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

    if(sum%4==0):
        print("Yes")
    else:
        print("No")
