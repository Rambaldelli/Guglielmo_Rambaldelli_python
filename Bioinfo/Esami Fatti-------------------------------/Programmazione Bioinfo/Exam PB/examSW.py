match={'A':{'G':0,'T':0,'C':0,'A':1},'G':{'A':0,'G':1,'T':0,'C':0},'T':{'A':0,'T':1,'C':0,'G':0},'C':{'A':0,'C':1,'G':0,'T':0}}

s1=['A','A','T','T','T','C']
s2=['T','T','C','G']

gap=-1

ms=0
mx=0
my=0
n=len(s1)+1
m=len(s2)+1

mat=[[0 for i in range(n)]for j in range(m)]
tr=[[0 for i in range(n)]for j in range(m)]

for i in range(1,m-1):
	for j in range(1,n-1):
		su=mat[i-1][j]+gap
		sl=mat[i][j-1]+gap
		sd=mat[i-1][j-1]+match[s1[j-1]][s2[i-1]]
		mat[i][j]=max(su,sl,sd,0)
		if mat[i][j]>ms:
			ms=mat[i][j]
			mx=j
			ms=i
		if mat[i][j]==su:
			tr[i][j]='up'
		elif mat[i][j]==sl:
			tr[i][j]='left'
		elif mat[i][j]==sd:	
			tr[i][j]='diagonal'
print('max score')
print(ms)
print('score position')
print(mx,my)
print('matrix')
print(mat)
print('traceback')
print(tr)
