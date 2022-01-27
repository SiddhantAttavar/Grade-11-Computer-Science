'''
WAP to input two matrices and perform matrix subtraction (Check if both the matrices are of 
same order r1==r2 and c1==c2 and display an appropriate message if they are not)
'''

r1 = int(input('Enter first matrix rows: '))
c1 = int(input('Enter first matrix columns: '))
a = []
for i in range(r1):
	a.append([])
	for j in range(c1):
		a[i].append(int(input('Enter a number: ')))

r2 = int(input('Enter second matrix rows: '))
c2 = int(input('Enter second matrix columns: '))
b = []
for i in range(r1):
	b.append([])
	for j in range(c1):
		b[i].append(int(input('Enter a number: ')))

if r1 != r2 or c1 != c2:
	print('Dimensions not matching')
else:
	c = []
	for i in range(r1):
		c.append([])
		for j in range(c1):
			c[i].append(a[i][j] - b[i][j])
	
	for row in c:
		for i in row:
			print(i, end = ' ')
		print()
