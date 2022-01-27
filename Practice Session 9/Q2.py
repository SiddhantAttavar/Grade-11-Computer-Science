'''
(a) WAP to input the below matrix (Check if it's a square matrix r==c otherwise display an 
appropriate message. Use the original matrix for all operations)
 22 13 42 22 13 42
 10 16 12 0 16 12 
 17 27 13 0 0 13
 (b) Find a upper triangular matrix and display it. Also compute the sum of the elements of this 
upper triangular matrix
 (c) Find the lower triangular matrix and count the even numbers in this lower triangular matrix
 (d) Display the odd numbers in both the diagonals (Principal diagonal/ Left diagonal :22,16,13 
 i==j Secondary diagonal/ Right diagonal: 42,16, 17 i+j ==r )
 (e) Display the upper half of the matrix
 22 13 42
 16 12 
 13
 (f) Display the border/boundary elements
22 13 42
10 12
17 27 1
'''

r = int(input('Enter no. of rows: '))
c = int(input('Enter no. of columns: '))

if r != c:
	print('Not a square matrix')
	exit()

a = []
for i in range(r):
	a.append([])
	for j in range(c):
		a[i].append(int(input('Enter a no.: ')))

b = []
s = 0
for i in range(r):
	b.append([0] * i)
	for j in range(i, r):
		b[i].append(a[i][j])
		s += a[i][j]

print('Sum or upper triangluar matrix:', s)

c = []
e = 0
for i in range(r):
	c.append([])
	for j in range(i + 1):
		c[i].append(a[i][j])
		if a[i][j] % 2 == 0:
			e += 1
	c.append([0] * (r - i - 1))
	e += r - i - 1

print('Even numbers in lower triangular matrix:', e)

o = 0
for i in range(r):
	if a[i][i] % 2 == 1:
		o += 1
	if a[i][r - i - 1] % 2 == 1:
		o += 1

print('Odd numbers in diagonals:', o)

for i in range(r):
	for j in range(i, r):
		print(a[i][j], end = ' ')
	print()

for j in range(r):
	print(a[0][j], end = ' ')
print()

for i in range(1, r - 1):
	print(a[i][0], a[i][r - 1])

for j in range(r):
	print(a[r - 1][j], end = ' ')
