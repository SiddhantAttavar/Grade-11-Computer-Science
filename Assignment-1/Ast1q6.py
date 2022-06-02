# Write a program to find the sum of the given series upto n terms:(Input x as an integer)
# 1 + x^2 / 2! + x^4 / 4! + x^6 / 6! + ... + x^n / n!

# Take input
x = int(input('Enter the value of x: '))
n = int(input('Enter the value of n: '))

# Initialize variables
exponent = 1
factorial = 1
seriesSum = 1

# Calculate result
for i in range(2, n + 1, 2):
    seriesSum += exponent / factorial
    exponent *= x * x
    factorial *= i * (i + 1)

# Print the result
print('The final sum is:', seriesSum)

'''Output:
Enter the value of x: 2
Enter the value of n: 5
The final sum is: 2.6666666666666665
'''