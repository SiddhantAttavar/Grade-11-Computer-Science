# To find the sum of the following series:
# 1/2! + 2/4! + 3/6! + ......n/(n*2)!
# (sum of 3 terms is 0.5875)

# Take input
n = int(input('Enter the number of terms: '))

# Initialize the sum and current factorial
seriesSum = 0
currFactorial = 2

# Iterate through the series and update sum and current factorial
for i in range(1, n + 1):
    seriesSum += i / currFactorial
    currFactorial *= (2 * i + 1) * (2 * i + 2)

# Print the result
print('Sum of the series is:', seriesSum)
