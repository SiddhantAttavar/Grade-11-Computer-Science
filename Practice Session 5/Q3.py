# Write a program that takes the month number from the user and 
# prints the number of days in that month. 
# Any other number other than 1 to 12 is invalid. 

# Create an array for number of days in the month
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Take input and display result
month = int(input('Enter the month number: '))
if month < 0 or month > 12:
    print('Invalid input')
else:
    print(f'The number of days in the month is {monthDays[month - 1]}')