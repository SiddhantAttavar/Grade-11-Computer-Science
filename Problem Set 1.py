# Program 1
# Accept the height of a person in cms and convert that to inches and feet. 
# (1 foot=12 inches, 1 inch=2.54 cms)
heightCms = float(input('Enter your height in cms: '))
print(f'Inches: {heightCms / 2.54:.2f}')
print(f'Feet: {heightCms / 12:.2f}')
print()

# Program 2
# Accept the base and height of a triangle and calculate the area. 
# (area of a triangle = 1/2bh - b is the base and h is the height)
base = int(input('Enter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))
print(f'Area: {base * height / 2:.2f}')
print()

# Program 3
# Accept the dividend and divisor as positive integers and find the quotient and
# remainder. Assume that the divisor is entered as a non zero number for this program.
dividend = int(input('Enter the dividend: '))
divisor = int(input('Enter the divisor: '))
print(f'Quotient: {dividend // divisor}')
print(f'Remainder: {dividend % divisor}')
print()