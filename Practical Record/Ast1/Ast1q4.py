# Program to print the first n numbers of fibonacci series 
# Sample input: 10 
# Sample output: 
# The first 10 terms of Fibonacii series are: 
# 0 1 1 2 3 5 8 13 21 34

# Take input
n = int(input('Enter the number of terms: '))
print('The first', n, 'terms of the Fibonacci series are:')

# Calculate the values of the Fibonacci series
a, b = 0, 1
print(a, b, end = ' ')
for i in range(n - 2):
    a, b = b, a + b
    print(b, end = ' ')

'''Output:
Enter the number of terms: 10
The first 10 terms of the Fibonacci series are:
0 1 1 2 3 5 8 13 21 34
'''