'''
This program inputs a list of numbers and performs operations:
 - Reverses the contents without creating a new list. 
 - Find the smallest and the largest number divisible by 5 in this list
'''

# Import variables
from math import inf

# Take input and reverse
a = list(map(int, input('Enter the list items: ').split()))
n = len(a)
for i in range(n // 2):
	a[i], a[n - i - 1] = a[n - i - 1], a[i]

print('Reversed list:', a)

# Find min and max
maxN = -inf
minN = inf
for i in a:
	if i % 5 == 0:
		if i < minN:
			minN = i
		if i > maxN:
			maxN = i

# Display output
if minN == inf:
	print('There are no numbers divisible by 5')
else:
	print('The smallest and largest number divisible by 5 are' , minN, 'and', maxN, '.')
