# Write a program to input 10 numbers from the keyboard and
# find the largest number and the smallest number.

# Take the first number as input and initialize minNum and maxNum
nums = list(map(int, input('Enter the numbers number: ').split()))

minNum = maxNum = nums[0]
n = 10

for i in range(1, len(nums)):
    # Update the min and max
    if nums[i] < minNum:
        minNum = nums[i]
    elif nums[i] > maxNum:
        maxNum = nums[i]

# Print the result
print(f'Minimum number: {minNum}')
print(f'Maximum number: {maxNum}')
