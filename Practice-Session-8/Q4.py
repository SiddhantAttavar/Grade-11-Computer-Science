# Write a menu driven program in Python to do the following tasks by taking 
# choice as input from the user :
# a. Print first n odd numbers in descending order
# b. Print the series 1    4    7    10........40
# c. Print the series 1   -4    7    -10....... -40

print('''Welcome to the menu driven program.
A: Print first n odd numbers in descending order
B: Print the series 1    4    7    10........40
C: Print the series 1   -4    7    -10....... -40
Other: Exit''')

op = input('Enter the operation (A/B/C/Other): ').upper()
while op in 'ABC':
	if op == 'A':
		# The user wants to do the first operation
		n = int(input('Enter the number of odd numbers to be printed: '))
		print(*range(2 * n - 1, 0, -2))
	elif op == 'B':
		# The user wants to do the second operation
		print(*range(1, 41, 3))
	elif op == 'C':
		# The user wants to do the third operation
		print(*(-x if i % 2 == 1 else x for i, x in enumerate(range(1, 41, 3))))
	op = input('Enter the operation (A/B/C/Other): ').upper()
