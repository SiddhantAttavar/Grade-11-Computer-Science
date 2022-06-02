# Accept a 5 worded sentence and print only the last alphabet
# of every word (should not be full stop or comma or any other special character.)

# Iterate throught words
for word in input('Enter a sentence: ').split():
    # Iterate through letters
    for letter in word[::-1]:
        # Check if letter is alphabet
        if letter.isalpha():
            # Print last alphabet
            print(letter)
            break

'''Output:
Enter a sentence: one two2 three. four, five$
e
o
e
r
e
'''