# Program to find the sum and count of numbers divisible by 6 and 9 in the range 
# input by the user. Also display these numbers with 3 numbers printed in a line.
# Sample input : 
# Lower = 5 
# Upper = 105 
# Sample output: 
# 18 36 54 
# 72 90 
# The sum and count of numbers divisible by 6 and 9 in the range 5 to 105 are 270 
# and 5 

# Take input
lower = int(input('Lower: '))
upper = int(input('Upper: '))

# Find the sum and count of numbers divisible by 6 and 9 in the range
finalSum = 0
finalCount = 0

# Find all numbers divisible by 6 in the given range
for i in range(lower, upper + 1):
    if i % 18 == 0:
        print(i, end = ' ')
        finalCount += 1
        finalSum += i

        if finalCount % 3 == 0:
            print()
if finalCount % 3 != 0:
    print()

# Print the result
print('The sum and count of numbers divisible by 6 and 9 in the range', end = ' ')
print(lower, 'to', upper, 'are', end = ' ')
print(finalSum, 'and', finalCount)

'''Output:
Lower: 5
Upper: 105
18 36 54 
72 90
The sum and count of numbers divisible by 6 and 9 in the range 5 to 105 are 270 and 5
'''