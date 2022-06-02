'''
6. Write a program to print bill for the customers of High Tech Retail. 
The product details (product name, price) are stored in  a list named 
product = [[p1,1200], [p2,2300], [p3,1700], [p4,1950]]. 
Input the details (product name, quantity) of the products purchased, 
store it in a nested list named purchases,
'''
product = [['p1',1200], ['p2',2300], ['p3',1700], ['p4',1950]]
purchases = []
totalBillAmount = 0
while True:
	name = input('Enter product name or <Enter> to exit: ')
	if not name:
		break
	quantity = int(input('Enter product quantity: '))
	purchases.append([name, quantity])
	for prodName, cost in product:
		if prodName == name:
			totalBillAmount += cost * quantity
			break
	else:
		print('Product not found')
	print('Name', '\t', 'Quantity')
	for prodName, qty in purchases:
		print(prodName, '\t', qty)
print('Total bill amount: ', totalBillAmount)
