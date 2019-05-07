seq1=input('seq1')
seq2=input('seq2')
gap=-1
ma=1
ms=-1
l1=len(seq1)+1
l2=len(seq2)+1
ma = [[0 for _ in range(l1)] for _ in range(l2)]
mt = [['0' for _ in range(l1)] for _ in range(l2)]
def compare(a,b):
	if a==b:
		return(ma)
	elif a!=b:
		return(ms)
	else:
		return(gap)
for i in range(1,l1+1):
	for j in range(1,l2+1):
		diag = ma[i-1][j-1] + int(compare(seq1[i-1], seq2[j-1]))
		up = ma[i][j-1] + gap
		left = ma[i-1][j] + gap
print(m1)



