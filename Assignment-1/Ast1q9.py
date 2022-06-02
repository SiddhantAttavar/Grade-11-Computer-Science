# Accept the string “Scientifica@NPSINR 2021-22 is a virtual fest”
# Find the number of upper-and lower-case alphabets, lower case vowels, digits, special characters
# and their counts from the above string and display in a neat format with suitable messages. 

# Take input and initialize the variables
string = input('Enter the string: ')
lowerCase = 0
upperCase = 0
lowerCaseVowels = 0
digits = 0
specialChars = 0

# Iterate throught string
for c in string:
    if c.islower():
        lowerCase += 1
        if c in 'aeiou':
            lowerCaseVowels += 1
    elif c.isupper():
        upperCase += 1
    elif c.isdigit():
        digits += 1
    else:
        specialChars += 1

# Print the results
print('The number of lowercase alphabets is:', lowerCase)
print('The number of uppercase alphabets is:', upperCase)
print('The number of lowercase vowels is:', lowerCaseVowels)
print('The number of digits is:', digits)
print('The number of special characters is:', specialChars)

'''Output:
Enter the string: Scientifica@NPSINR 2021-22 is a virtual fest
The number of lowercase alphabets is: 24
The number of uppercase alphabets is: 7
The number of lowercase vowels is: 11
The number of digits is: 6
The number of special characters is: 7
'''