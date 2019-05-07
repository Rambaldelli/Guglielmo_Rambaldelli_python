a=[]
for i in range(10):
	a.append(int(input('numerino plz')))
	print(a)
for j in range(len(a))[1:]:
	key=a[j]
	i=j-1
	print(key)
	while i >= 0 and a[i] > key:
		a[i+1]=a[i]
		i=i-1
	a[i+1]=key
print(a)
	

