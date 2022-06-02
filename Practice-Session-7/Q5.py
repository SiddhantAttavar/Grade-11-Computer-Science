# Write a program using loop that asks the user to enter a multiple of 10. 
# If the number entered is not a multiple of 10, then display an
# appropriate message and  ask them to enter a number again. Do not stop until a multiple of 10 
# is entered. Print a Congratulatory message at end.
while (x := int(input('Enter a multiple of 10: '))) % 10 != 0:
    print(f'{x} is not a multiple of 10')
print(f'Congratulations! {x} is a multiple of 10')