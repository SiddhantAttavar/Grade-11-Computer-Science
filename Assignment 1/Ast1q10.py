# Accept the following sentence and find the number of Palindromic words in it. 
# (Irrespective of their case)
# Some countries have laws that punish crimes with an eye for an eye. 
# They insist on civic responsibilities. 
# If they want this on people's radar, proper rules should be framed

# Initialize count
count = 0

# Iterate through words
for word in input('Enter a sentence: ').lower().split():
    newWord = ''
    # Iterate through each letter in word
    for letter in word:
        # If letter is a letter, add to newWord
        if letter.isalnum():
            newWord += letter

    # Check if word is palindromic
    if newWord == newWord[::-1]:
        # Increment count
        count += 1

# Print the result
print('Number of palindromic words:', count)

'''Output:
Enter a sentence: Some countries have laws that punish crimes with an eye for an eye. They insist on civic responsibilities. If they want this on people's radar, proper rules should be framed
Number of palindromic words: 2
'''