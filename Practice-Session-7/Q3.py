# Write a program to input n numbers and print the sum of even and odd numbers.
# Take input
nums = list(map(int, input('Enter the numbers: ').split()))
evenNums = []
oddNums = []

# Iterate through list and find even numbers and odd numbers
for num in nums:
    if num % 2 == 0:
        evenNums.append(num)
    else:
        oddNums.append(num)

# Calculate the sum of even and odd numbers
# Display the result
print(f'Sum of even numbers is = {" + ".join(map(str, evenNums))} = {sum(evenNums)}')
print(f'Sum of odd numbers is = {" + ".join(map(str, oddNums))} = {sum(oddNums)})')