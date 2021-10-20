# Accept an integer from the user. 
# If the number is negative, print the square of the number. 
# If the number is positive, print the cube of the number. 
# If the number is 0, print Zero. 
# Display with suitable messages. 

# Take input
num = int(input('Enter the number: '))
if num < 0:
    # Print the square of the number
    print(num * num)
elif num > 0:
    # Print the cube of the number
    print(num * num * num)
else:
    # Print 0
    print(0)