# Program 1
# Write a program to initialize values into 4 strings. Display the sizes of each.
# Initialize the strings
a = 'Varun\'s book\t'
b = '\t\\\"'
c = '''Macintosh
OS'''
d = 'Optical\
	Fibre'

# Print the size of the strings
print(f'The size of a is {len(a)}')
print(f'The size of b is {len(b)}')
print(f'The size of c is {len(c)}')
print(f'The size of d is {len(d)}')

# Program 2
# Write a program to input the temperature in Fahrenheit and in Celsius and print its equivalent in  Celsius and Fahrenheit respectively.
tempCelcius = float(input('Enter the temperature in Celsius: '))
print(f'The temperature in Fahrenheit is {(1.8 * tempCelcius) + 32}')

tempFarenheit = float(input('Enter the temperature in Fahrenheit: '))
print(f'The temperature in Celcius is {(tempFarenheit - 32) / 1.8}')

# Program 3
# Write a program to input a 4 digit number and print the sum of the digits.                        
# (Note use % operator) Also print the square and cube of each digit in a line and for every digit , one below the other. 
num = int(input('Enter the number: '))
digits = [
	(num - (num % 1000)) // 1000, 
	((num % 1000) - (num % 100)) // 100, 
	((num % 100) - (num % 10)) // 10, 
	num % 10
]

print(f'The sum of the number {num} is {sum(digits)}')

# Caulculate the square and cubes
squares = list(map(lambda x: x * x, digits))
cubes = list(map(lambda x: x * x * x, digits))

# Print the results
print('Digit\tSquare\tCube')
print(f'{digits[0]}\t{squares[0]}\t{cubes[0]}')
print(f'{digits[1]}\t{squares[1]}\t{cubes[1]}')
print(f'{digits[2]}\t{squares[2]}\t{cubes[2]}')
print(f'{digits[3]}\t{squares[3]}\t{cubes[3]}')

# Program 4
# Write a program to accept the marks scored by a student in 4 subjects, calculate the total and average and display
scores = [
	int(input('Enter your computer science marks: ')),
	int(input('Enter your physics marks: ')),
	int(input('Enter your maths marks: ')),
	int(input('Enter your chemistry marks: ')),
]

# Print the results
print('Subjects\t\tMarks')
print(f'Computer science\t{scores[0]}')
print(f'Physics\t\t\t{scores[1]}')
print(f'Maths\t\t\t{scores[2]}')
print(f'Chemistry\t\t{scores[3]}')
print(f'The total is {sum(scores)} and the average is {sum(scores) / len(scores)}')