# Write a program to input a number and print whether the number is a neon number.
# A number is said to be a neon if the sum of all the digits of square of a number is
# equal to the entered number
# Take input
n = int(input('Enter the number: '))
# Initialize sum and calculate the square of the number
square = n * n
squareSum = 0

# Calculate the sum of each digit of the square of the number
while square > 0:
    squareSum += square % 10
    square //= 10

# Check if the number is a neon number
if squareSum == n:
    print(f'The number {n} is a neon number')
else:
    print(f'The number {n} is not a neon number')