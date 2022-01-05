# Input a number and check if it is prime or not.
n = int(input('Enter a number: '))
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print(f'{n} is not prime')
        break
else:
    print(f'{n} is prime')

# Input a number and check if it is an armstrong number or not.
n = int(input('Enter a number: '))
digitCubeSum = 0
orig = n
while n > 0:
    digitCubeSum += (n % 10) ** 3
    n = n // 10
if orig == digitCubeSum:
    print(f'{orig} is an armstrong number')
else:
    print(f'{orig} is not an armstrong number')

# Generate the first n fibonnaci numbers.
n = int(input('Enter a number: '))
a, b = 0, 1
print(f'The first {n} fibonnaci numbers are: ', end = '')
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
