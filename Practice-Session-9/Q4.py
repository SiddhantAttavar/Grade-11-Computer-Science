'''
WAP to input a matrix and compute the row sum and column sum of each row and column and 
store them in two linear lists named lst_rowsum and lst_colsum.
Lst_rowsum = [ row1sum,row2sum.....]
'''

n = int(input('Enter no. of rows: '))
m = int(input('Enter no. of columns: '))

a = []
for i in range(n):
	a.append([])
	for j in range(m):
		a[i].append(int(input('Enter a no.: ')))

lst_rowsum = []
for i in range(n):
	lst_rowsum.append(0)
	for j in range(m):
		lst_rowsum[i] += a[i][j]

for i in lst_rowsum:
	print(i, end = ' ')
print()

lst_colsum = []
for j in range(m):
	lst_rowsum.append(0)
	for i in range(n):
		lst_rowsum[j] += a[i][j]

for j in lst_colsum:
	print(j, end = ' ')
print()
