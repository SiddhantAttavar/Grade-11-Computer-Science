# Assign 15 integers (negative, positive and zeroes) to a list Lst.
# Shift all the positive odd integers to the right of a new list Lst1
# and rest of the integersto the left of Lst1.
# (Note: Assign zeroes and repeating numbers to the list)
# Display the original and the new lists.
# Sample Input to assign: L = [12,-5,67,0,4,78,9,0,-34,-5,5,7,1,0,89]
# Sample Output: L1 = [67,9,5,7,1,89,12,-5,0,4,78,0,-34,-5,0]

l = eval(input("Enter a list of numbers: "))

positiveOddList = []
otherList = []
for i in l:
	if i > 0 and i % 2 != 0:
		positiveOddList.append(i)
	else:
		otherList.append(i)

finList = positiveOddList + otherList
print("Original list: ", l)
print("New list: ", finList)

'''Ouptut:
Enter a list of numbers: [12,-5,67,0,4,78,9,0,-34,-5,5,7,1,0,89]
Original list:  [12, -5, 67, 0, 4, 78, 9, 0, -34, -5, 5, 7, 1, 0, 89]
New list:  [67, 9, 5, 7, 1, 89, 12, -5, 0, 4, 78, 0, -34, -5, 0]
'''