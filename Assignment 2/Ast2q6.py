'''
6. The Great Indian Library stores the book details 
(bookid, number of total copies, number of copies remaining) in a
tuple named bookdet.
bookdet = (('Fic101',5,[5]) , ('Lit257',4,[4]) , ('SciFi333',4,[4]), 
('Autobi243',6,[6])). 
It also stores the member details (memid,password) in a list named memdet.
memdet = [(m222,'AHK101'),(m223,'fgdHk'),(m224,'iuytr')]
Write a menu driven program to automate the issue process. 
(a) Every time a member comes, he/she is asked to login. The login 
credentials are checked in the memdet list and appropriate message is 
displayed.
(b) If the member logs in successfully, the list of books id (that 
are available for issue i.e number of copies remaining > 0) are displayed .
(c) The member chooses a book and enters his member id and book id. 
Issue the book and store the book id along with member id in a nested list
Issuedetails. Update the copies remaining in the bookdet accordingly. 
If the member id already exists in the Issuedetails, update the existing 
issue details of the member in the Issuedetails by adding the new book id 
in the respective sublist of member.
'''
bookdet = (('Fic101',5,[5]) , ('Lit257',4,[4]) , ('SciFi333',4,[4]), 
('Autobi243',6,[6]))
memdet = [('m222','AHK101'),('m223','fgdHk'),('m224','iuytr')]
Issuedetails = []
while True:
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
	for user in Issuedetails:
		if user[0] == memid:
			user[1].append(bookid)
			print('Your books:', ', '.join(user[1]))
			break
	else:
		Issuedetails.append([memid, [bookid]])
		print('Your books:', ', '.join(Issuedetails[-1][1]))
