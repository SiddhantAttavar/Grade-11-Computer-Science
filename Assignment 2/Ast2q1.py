# Input a list of 10 elements (numbers) and display the
# original list and each occurrence of all the two-digit 
# numbers (including negative 2-digit numbers) in the list.
# Also display the count and sum of them.(Input numbers can be repeated)

# Take input
l = []
for i in range(10):
	l.append(int(input("Enter a number: ")))

# Display original list
print("Original list: ", *l)

# Display each occurrence of two-digit numbers
finlist = []
sumNums = 0
for i in l:
	if i >= 10 and i <= 99:
		finlist.append(i)
		sumNums += i
print("Occurrence of two-digit numbers: ", *finlist)
print("Count of two-digit numbers: ", len(finlist))
print("Sum of two-digit numbers: ", sumNums)

'''Output:
Enter a number: 5
Enter a number: 6
Enter a number: 2
Enter a number: 164
Enter a number: 16 
Enter a number: 45 
Enter a number: 15
Enter a number: 65
Enter a number: 2
Enter a number: 154
Original list:  5 6 2 164 16 45 15 65 2 154
Occurrence of two-digit numbers:  16 45 15 65
Count of two-digit numbers:  4
Sum of two-digit numbers:  141
'''
