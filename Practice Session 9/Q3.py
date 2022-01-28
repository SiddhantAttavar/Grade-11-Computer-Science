'''
WAP to input a square matrix with odd dimension and perform the following:
 (a) Display the middle row and middle column elements and compute their sum
 (b) Display the product of right diagonal elements
'''

n = int(input('Enter side length: '))
if n % 2 == 0:
	print('Input odd number')
	exit()

a = []
for i in range(n):
	a.append([])
	for j in range(n):
		a[i].append(int(input('Enter a number: ')))

s = 0
print('Middle row: ')
for j in range(n):
	print(a[n // 2][j], end = ' ')
	s += a[n // 2][j]

print('Middle row: ')
for i in range(n):
	print(a[i][n // 2], end = ' ')
	s += a[i][n // 2]

s -= a[n // 2][n // 2]
print('Sum:', s)

p = 1
for i in range(n):
	p *= a[i][n - i - 1]
print('Product:', p)
