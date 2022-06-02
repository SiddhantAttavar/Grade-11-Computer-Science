# Write a program to input a single digit and print it in words. 

# Map digits to their words
digitMap = [
    'zero',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

# Take input and display output
digit = int(input('Enter the digit: '))
if digit < 0 or digit >= 10:
    print('Invalid input')
else:
    print(f'The digit is {digitMap[digit]}')
