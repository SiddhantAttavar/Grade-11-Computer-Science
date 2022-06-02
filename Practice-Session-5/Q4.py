# Accept an arithmetic operator(+,-,*,%,/,//,**) +
# and two numeric operands from the user 
# and display suitable result with proper message according to the operation chosen by the user. 

# Take input
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
op = input('Enter the operation: ')

# Calculate and display result
if op == '+':
    print(f'The result is {x + y}')
elif op == '-':
    print(f'The result is {x - y}')
elif op == '*':
    print(f'The result is {x * y}')
elif op == '/':
    print(f'The result is {x / y}')
elif op == '//':
    print(f'The result is {x // y}')
elif op == '%':
    print(f'The result is {x % y}')
elif op == '**':
    print(f'The result is {x ** y}')
else:
    print('Invalid input')
