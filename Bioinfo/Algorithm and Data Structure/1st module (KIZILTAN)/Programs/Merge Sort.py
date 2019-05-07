import math
a=[3,5,2,6,3,4,3,5]
#for i in range(10):
#	a.append(input('numerino plz'))
n=len(a)
def merge(a,p,q,r):
	l=[]
	m=[]
	for c in range(q):
		l.append(a[c])
		m.append(a[c+q])
	l.append(math.inf)
	m.append(math.inf)
	i=0
	j=0
	for k in range(r):
		if l[i]<=m[j]:
			a[k]=l[i]
			i=i+1
		else:
			a[k]=m[j]
			j=j+1

def merges(a,p,r):
	if p<r:	
		q=int((p+r)/2)
		print(p)
		print(q)
		print(r)
		merges(a,p,q)
		merges(a,q+1,r)
		merge(a,p,q,r)

print(merges(a,0,n))

	
