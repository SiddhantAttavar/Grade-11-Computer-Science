# Write a program to input a three digit number and check if its a armstrong number.
# Armstrong number is a number that is equal to the sum of cubes of its digits

# Take input and calculate sum of cube of digits
num = input('Enter a number: ')
digitCubeSum = int(num[0]) ** 3 + int(num[1]) ** 3 + int(num[2]) ** 3

# Check if they are equal and display result
if digitCubeSum == int(num):
    print('It is an Armstrong number')
else:
    print('It is not a Armstrong number')