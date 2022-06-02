inputString = input('Enter a string: ')

alphaCount = 0
numberCount = 0
specialCount = 0

for char in inputString:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        alphaCount += 1
    elif '0' <= char <= '9':
        numberCount += 1
    else:
        specialCount += 1

print(f'The number of alphabets are: {alphaCount}')
print(f'The number of digits are: {numberCount}')
print(f'The number of special characters are: {specialCount}')
