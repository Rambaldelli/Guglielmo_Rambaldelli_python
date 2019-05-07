with open('insulin.gbk') as a:
	flag=0
	s=[]
	for i in a:
		k=" ".join(i.split())
		j=k.split(' ')
		if j[0]=='ACCESSION':
			h=j[1]
		elif j[0]=='ORGANISM':
			o=j[1]+' '+j[2]
		elif j[0]=='ORIGIN':
			flag=1
		elif flag==1:
			s.append(''.join(j[1::]))
			p='\n'.join(s)
	print('>'+h+'|'+o)
	print(p)
	

			
