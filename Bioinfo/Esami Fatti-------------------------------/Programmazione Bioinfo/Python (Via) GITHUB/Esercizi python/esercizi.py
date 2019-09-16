import math
print('es1')
x=7
print(x)
y=3.14
i=0
while i==0:
	if x%2==0:
		print('even')
	z=(x+y)/2
	print(z)
	dx=abs(z-x)
	dy=abs(z-y)
	print(x,'dist', dx)
	print(y,'dist',dy)
	md=dx+dy/2
	print(md)
	y=(y+2)-1
	i=1
x1=3
x2=4
y1=6
y2=5
dxy=math.sqrt((x1-y1)**2+(x2-y1)**2)
print(dxy)







