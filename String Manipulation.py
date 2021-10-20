# Print the characters of an inputed string
s = input('Enter a string: ')
for c in s:
    print(c)

# Print the characters of an inputed string in reverse order
s = input('Enter a string: ')
for c in reversed(s):
    print(c)

# Print alternate characters of an inputed string
s = input('Enter a string: ')
for c in s[::2]:
    print(c)