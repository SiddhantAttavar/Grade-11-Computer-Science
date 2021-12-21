'''
A bank stores it's customer details in a nested dictionary named 'Account' such that the 
 accountid is a key and the value is a dictionary with name and balance as the keys. Write 
 a menu based program to input the accountid, type of transaction and transaction amount 
 and update the records as per the instructions given below:
 If type = 'd' , it is considered to be a deposit and the amount is added to the balance.
 If type = 'w', it is considered to be a withdrawal and the amount is deducted from 
 balance. In case of withdrawal, if the balance is going below 1000, then the transaction is 
 cancelled and appropriate message is displayed. 
 If type = 'b', the current account balance of that account holder gets displayed. If the 
 accountid does not exist, the customer details are taken as input and added in the 
 'Account' dictionary as a new key value pair
'''

Account = {}

while True:
	op = input('Deposit / Withdraw / Display balance / Exit - D/W/B/E: ').lower()
	accountid = int(input('Enter account id: '))
	if op == 'd':
		amount = int(input('Enter deposit amount: '))
		Account[accountid]['balance'] += amount
	elif op == 'w':
		amount = int(input('Enter withdrawal amount: '))
		if Account[accountid]['balance'] - amount < 1000:
			print('Withdrawal cancelled, low balance')
		else:
			Account[accountid]['balance'] -= amount
	elif op == 'b':
		if accountid in Account:
			print(Account[accountid]['name'], 'balance is', Account[accountid]['balance'])
		else:
			name = input('Enter name: ')
			Account[accountid] = {
				'name': name,
				'balance': 0
			}
