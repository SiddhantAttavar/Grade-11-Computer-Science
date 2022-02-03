'''
This program performs operations:
 - Authentice user
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
