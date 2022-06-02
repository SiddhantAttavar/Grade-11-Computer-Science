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
