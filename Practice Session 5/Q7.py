# Input age of the dog (integer) and convert to equivalent human years according to the following rule. 
# If age of dog 1 year=>14 human years, 2 years=>22 human years, 
# then for every added year, equivalent 5 human years are added.  

# Take input
dogYears = int(input('Enter the age of the dog: '))

# Check for invalid input and then calculate the age to display to the user
if dogYears < 0:
    print('Invalid input')
elif dogYears == 1:
    print('The age of the dog in human years is 14')
else:
    print(f'The age of the dog in human years is {22 + 5 * (dogYears - 2)}')