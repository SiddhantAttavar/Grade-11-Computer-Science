'''
This program inputs a list of elements and performs operations:
 - Shift all the positive odd integers to the right of a new list
 - Shift all other integers to the left of the list
 - Display the original and the new lists
'''

# Take input
l = eval(input("Enter a list of numbers: "))

# Divide into two lists
positiveOddList = []
otherList = []
for i in l:
	if i > 0 and i % 2 != 0:
		positiveOddList.append(i)
	else:
		otherList.append(i)

# Display final list
finList = positiveOddList + otherList
print("Original list: ", l)
print("New list: ", finList)

'''Ouptut:
Enter a list of numbers: [12,-5,67,0,4,78,9,0,-34,-5,5,7,1,0,89]
Original list:  [12, -5, 67, 0, 4, 78, 9, 0, -34, -5, 5, 7, 1, 0, 89]
New list:  [67, 9, 5, 7, 1, 89, 12, -5, 0, 4, 78, 0, -34, -5, 0]
'''
