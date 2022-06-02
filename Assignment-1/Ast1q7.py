# Print all the Palindromic Prime numbers in the range 200 to 400.
# A palindromic prime number is the number which is a palindrome as well as prime.
# Sample Answer: In the given range, 353 is a palindrome as well as prime number 
# while 202 is a palindrome but not palindromic prime. 
# Print the output values five in each line.

# Initialize count
count = 0

# Iterate through all values
for i in range(200, 401):
    # Check if the number is a palindrome
    if str(i) == str(i)[::-1]:
        # Check if the number is prime
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            # Print the number
            print(i, end = ' ')
            # Increment count
            count += 1
            # Check if count is equal to 5
            if count == 5:
                # Reset count
                count = 0
                # Print a new line
                print()

'''Output:
313 353 373 383
'''