# Accept the following sentence and find the number of Palindromic words in it. 
# (Irrespective of their case)
# Some countries have laws that punish crimes with an eye for an eye. 
# They insist on civic responsibilities. 
# If they want this on people's radar, proper rules should be framed

# Initialize count
count = 0

# Iterate through words
for word in input('Enter a sentence: ').lower().split():
    # Check if word is palindromic
    if word == word[::-1]:
        # Increment count
        count += 1

# Print the result
print('Number of palindromic words:', count)

'''Output:
Enter a sentence: Some countries have laws that punish crimes with an eye for an eye. They insist on civic responsibilities. If they want this on people's radar, proper rules should be framed
Number of palindromic words: 2
'''