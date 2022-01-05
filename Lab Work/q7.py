'''
7. Create a dictionary month_dic whose keys are month name and values is 
the number of days in the corresponding months. 
Write a menu based program to perform the following operations:
a) Input month name and number of days from the user and store it in the 
dictionary.
c) Input number of days from the user and display all the months having 
those many days.
b) Display months with 31 days.
'''
month_dic = {}
while True:
	op = input('Enter A/B/C or E to exit: ')
	if op == 'A':
		monthName = input('Enter month name: ')
		monthDays = int(input('Enter no. of days: '))
		month_dic[monthName] = monthDays
		for month in month_dic:
			print(month, 'has', month_dic[month], 'days')
	elif op == 'B':
		days = int(input('Enter no. of days: '))
		for month in month_dic:
			if month_dic[month] == days:
				print(month, 'has', days, 'days')
	elif op == 'C':
		for month in month_dic:
			if month_dic[month] == 31:
				print(month, 'has 31 days')
	else:
		break
