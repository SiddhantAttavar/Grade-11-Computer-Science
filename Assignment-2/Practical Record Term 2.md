# Practical Record Term 2
 - Name: Siddhant Attavar
 - Class: 11B
 - Subject: Computer Science

## Question 1
```python
'''
This program inputs a list of elements and performs operations:
 - Display the original list
 - Display all occurences of two digit numbers
 - Display the count and sum of two digit numbers
'''

# Take input
l = []
for i in range(10):
	l.append(int(input("Enter a number: ")))

# Display original list
print("Original list: ")
for i in range(l):
	print(i)

# Display each occurrence of two-digit numbers
finlist = []
sumNums = 0
for i in l:
	if i >= 10 and i <= 99:
		finlist.append(i)
		sumNums += i
print("Occurrence of two-digit numbers: ")
for i in finlist:
	print(i)
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
```

## Question 2
```python
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
```

## Question 3
```python
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
```

## Question 4
```python
'''
This program Accept names of 5 students along with their marks, stores them to a nested list and performs operations:
 - Display the original list in tabular format
 - Search for a name and update the new mark
 - Display the updated list in tabular format
 - Display a suitable message if the name doesn't exist in Stu_Marks.
'''

# Take input
students = []
for i in range(5):
	students.append([input("Enter a name: "), int(input("Enter a mark: "))])

# Print original list
print("Original list: ")
print("Name\tMarks")
for i in students:
	print(i[0], '\t' , i[1])

# Update marks
name = input("Enter a name: ")
for i in students:
	if i[0] == name:
		i[1] = int(input("Enter a new mark: "))
		break
else:
	print("Name not found.")

'''Output:
Enter a name: Name1
Enter a mark: 100
Enter a name: Name2
Enter a mark: 90    
Enter a name: Name3
Enter a mark: 95    
Enter a name: Name4
Enter a mark: 97    
Enter a name: Name5
Enter a mark: 86
Original list: 
Name1 100
Name2 90
Name3 95
Name4 97
Name5 86
Enter a name: Name1
Enter a new mark: 79
'''
```

## Question 5
```python
'''
This program performs operations:
 - Add new items to the store
 - Remove an item from the store on the basis of product name input by the user
 - Update the price of a product taking the input of new price from the user
 - Display suitable message in case the item is not found for removal or updation
'''

product = [['p1',1200], ['p2',2300], ['p3',1700], ['p4',1950]]
while True:
	# Take input
	op = input('Enter A/B/C or E to exit: ')

	if op == 'A':
		# Add new items
		name = input('Enter product name: ')
		cost = int(input('Enter product price: '))
		product.append([name, cost])
	elif op == 'B':
		# Remove items
		name = input('Enter product name: ')
		for i in range(len(product)):
			if name == product[i][0]:
				product.pop(i)
				break
		else:
			print(name, 'not found')
	elif op == 'C':
		# Update price of items
		name = input('Enter product name: ')
		cost = int(input('Enter product price: '))
		for i in range(len(product)):
			if name == product[i][0]:
				product[i][1] = cost
				break
		else:
			print(name, 'not found')
	else:
		# Exit
		break
	
	# Display items
	print('Products:')
	print('Name', '\t', 'Price')
	for prodName, cost in product:
		print(prodName, '\t', cost)
```

## Question 6
```python
'''
This program performs operations: 
 - Authenticates a user
 - Displays books that are available for issue
 - Allows the member to choose a book and updates the copies remaining in the bookdet accordingly
'''

bookdet = (('Fic101',5,[5]) , ('Lit257',4,[4]) , ('SciFi333',4,[4]), 
('Autobi243',6,[6]))
memdet = [('m222','AHK101'),('m223','fgdHk'),('m224','iuytr')]
Issuedetails = []
while True:
	# Authenticate user
	username = input('Enter memid: ')
	password = input('Enter password: ')
	loggedIn = False
	for _ in range(3):
		for usr, pwd in memdet:
			if username == usr and password == pwd:
				print('Authenticated')
				loggedIn = True
				break
		if loggedIn:
			break
	else:
		print('Not authenticated')
		continue

	# Check it bool is available to borrow
	for book in bookdet:
		if book[2][0] > 0:
			print(book[0], 'available')
	memid = input('Enter memid: ')
	bookid = input('Enter book id: ')
	for book in bookdet:
		if book[0] == bookid:
			book[2][0] -= 1
			break
	else:
		print('Book not found')
		continue
	
	# Display users book
	for user in Issuedetails:
		if user[0] == memid:
			user[1].append(bookid)
			print('Your books:', ', '.join(user[1]))
			break
	else:
		Issuedetails.append([memid, [bookid]])
		print('Your books:', ', '.join(Issuedetails[-1][1]))
```

## Question 7
```python
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
```

## Question 8
```python
'''
This program inputs contact details and performs operations: 
 - Use appropriate in built function and arrange the contacts in alphabetical order
 - Modify the number of an existing contact
 - Delete a friend's record from the dictionary using his/her number
'''

# Take input
contact_det = {}
n = int(input('Number of friends: '))
for _ in range(n):
	name = input('Enter name: ')
	num = int(input('Enter mobile number: '))
	contact_det[name] = num

# Sort contacts
for k, v in sorted(contact_det.items()):
	print(k, ':', v)

while True:
	# Take input
	op = input('Modify / Delete / Exit - M/D/E: ').lower()

	if op == 'm':
		# Modify existing contact
		name = input('Enter name: ')
		num = int(input('Enter mobile number: '))
		if name in contact_det:
			contact_det[name] = num
		else:
			print(name, 'not found')
	elif op == 'd':
		# Delete contact
		num = int(input('Enter number: '))
		for k, v in contact_det.items():
			if v == num:
				name = k
				break
		else:
			print(num, 'not found')
		if name in contact_det:
			contact_det.pop(name)
	else:
		break
    
	# Display contacts
	for k, v in sorted(contact_det.items()):
		print(k, ':', v)
```

## Question 9
```python
'''
This program inputs the names of 5 cities along with their population and performs operations:
 - Create two new dictionaries Male population and Female population
 - Display the cities with male population greater than 40000.
 - Compute the average of women population without using any statistical module.
'''

# Take input
population = {}
malePopulation = {}
femalePopulation = {}
n = int(input('Enter number of cities: '))
for _ in range(n):
	city = input('Enter city: ')
	currPopulation = int(input('Enter population: '))
	population[city] = currPopulation

# Find male and female population
sumPopulation = 0
for k, v in population.items():
	malePop = int(0.52 * v)
	femalePop = v - malePop
	malePopulation[k] = malePop
	femalePopulation[k] = femalePop
	if malePop > 40000:
		print('The male population of', k, 'is greater than 40000')
	
	sumPopulation += femalePop

# Display output
print('The average population is', sumPopulation / n)
```

## Question 10
```python
'''
This program performs operations:
 - Authenticate user
 - Deposit amount to added to balance
 - Withdraw amount is deducted from user
 - Display current account balance of that account holder
'''

Account = {}
while True:
	# Take input
	op = input('Deposit / Withdraw / Display balance / Exit - D/W/B/E: ').lower()
	accountid = int(input('Enter account id: '))
	if accountid not in Account:
		name = input('Enter name: ')
		Account[accountid] = {
			'name': name,
			'balance': 0
		}
	
	if op == 'd':
		# Deposit
		amount = int(input('Enter deposit amount: '))
		Account[accountid]['balance'] += amount
	elif op == 'w':
		# Withdraw
		amount = int(input('Enter withdrawal amount: '))
		if Account[accountid]['balance'] - amount < 1000:
			print('Withdrawal cancelled, low balance')
		else:
			Account[accountid]['balance'] -= amount
	elif op == 'b':
		# Display balance
		print(Account[accountid]['name'], 'balance is', Account[accountid]['balance'])
```
