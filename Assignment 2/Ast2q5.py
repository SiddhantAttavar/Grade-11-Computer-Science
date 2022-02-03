'''
5. High Tech Retail stores the product details (product name, price) 
in  a list named product.
product = [[p1,1200], [p2,2300], [p3,1700], [p4,1950]]. 
Write a menu driven program:
(a) to add new items to the store
(b) to remove an item from the store on the basis of product name 
input by the user
(c) to update the price of a product taking the input of new price 
from the user
Display suitable message in case the item is not found for removal 
or updation.
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
