'''
This program generates 10 random integers in the range -10 to 10 and performs operations:
 - Find the square root of the positive elements
 - Find the square of the negative elements
 - Display all the lists
'''

# Generate random list
from math import sqrt
from random import randint
l = []
for i in range(10):
	l.append(randint(-10,10))

# Find square root of position elements and square of negative elements
sqr = []
sq = []
for i in l:
	if i > 0:
		sqr.append(int(sqrt(i)))
	elif i < 0:
		sq.append(i**2)

# Display output
print("Original list: ", l)
print("Square root of positive elements: ", sqr)
print("Square of negative elements: ", sq)

'''Output:
Original list:  [-2, -5, 2, -4, -6, -10, -5, 10, 6, 3]
Square root of positive elements:  [1, 3, 2, 1]
Square of negative elements:  [4, 25, 16, 36, 100, 25] 
'''
