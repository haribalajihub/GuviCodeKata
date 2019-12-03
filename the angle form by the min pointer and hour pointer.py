h,m=input().split()
h=int(h)
m=int(m)

if (h == 12): 
			h = 0
if (m == 60): 
			m = 0
			
hour = 0.5 * (h * 60 + m) 
minu = 6 * m 
			
angle = abs(hour - minu)
		
angle1 = min(360 - angle, angle) 
		
print(int(angle1))
