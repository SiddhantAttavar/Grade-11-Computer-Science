'''
Input a list of numbers and reverse the contents without creating a new list. 
Also find the smallest and the largest number divisible by 5 in this list. 
Display a suitable message if the numbers are not divisible by 5. 
Both the operations have to be performed without using any inbuilt function.
Sample input : [10,30,20,40,70]
Sample output: [70,40,20,30,10]
The smallest and largest number divisible by 5 are 10 and 70.
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
