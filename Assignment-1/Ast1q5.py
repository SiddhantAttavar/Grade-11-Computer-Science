# Program to check if an input number is a perfect number or not 
# perfect number - sum of proper divisors of a number excluding the number 
# equals to the number itself. 
# Eg: 6, 28, 496 etc

# Take input
n = int(input('Enter a number: '))

# Check if the number is a perfect number
sumOfDivisors = 0
for i in range(1, n):
    if n % i == 0:
        sumOfDivisors += i

# Print result
if sumOfDivisors == n:
    print('The number is a perfect number')
else:
    print('The number is not a perfect number')

'''Output:
Enter a number: 6
The number is a perfect number

Enter a number: 25
The number is not a perfect number
'''