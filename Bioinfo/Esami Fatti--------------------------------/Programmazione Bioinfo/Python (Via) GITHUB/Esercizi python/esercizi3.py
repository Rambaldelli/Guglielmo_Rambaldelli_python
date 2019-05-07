def inc(x):
	return x++
def add(x,y):
	return x+y
def add3(x,y,z):
	return x+y+z
def dist(x,y):
	import math
	dx=math.sqrt(x[0]**2-y[0]**2)
	dy=math.sqrt(x[1]**2-y[1]**2)
	c=[dx,dy]
	return c
def secD(a,b,c):
	import math
	D=b**2-4*c*a
	if D>0:
		D=math.sqrt(D)
		x1=(-b+D)/2*a
		x2=(-b-D)/2*a
		return x1,x2
	elif D==0:
		x=-b/(2*a)
		return(x)
	else:
		return('so solution')
def spastico(x,y):
	y1=y
	for i in range(x):
		y1=y1+y
	return y1	
def spastico2(x,y):
	y1=[]
	for i in range(x):
		y1.append(y)
	return y1	
def spasticoStyle(x,y,z):
	K=y
	for i in range(x-1):
		K=K+z
		K=K+y
	return K
	

