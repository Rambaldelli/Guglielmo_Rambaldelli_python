a='fire and ice'
A=list(a)
print(A)

for i in range(len(a)):	
	if i%2==0:
		print(A[i],'even')
	else:
		print(A[i],'odd')
k=int(len(A)/2)
print(k)
print(A[:k])
print(A[::-1])
print(A.count('i'),A.count('e'))

b=''.join(A)
print(b)
if b.find('fire'):
	print('si')
if b.find('re end'):
	print('si')
if b.find('re &'):
	print('si')

for j in range(len(a)):	
	if a[j]=='e':
		print(j,'first')
		break
		
	if a[-j]=='e': 
		print(-j,'last')
		break
