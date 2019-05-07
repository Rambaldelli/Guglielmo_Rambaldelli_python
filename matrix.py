def pretty_matrix(m):
    for i in m:
        print(i)

a=[[0 for col in range(5)]for row in range(3)]
a[0][2]='a'
pretty_matrix(a)
