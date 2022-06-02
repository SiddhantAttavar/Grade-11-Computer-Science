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
