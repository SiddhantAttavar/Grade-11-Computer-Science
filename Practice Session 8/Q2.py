# To print the multiplication tables of a range of numbers input by the user 
# (by accepting the lower limit and upper limit as input). 
# Print 5 multiples of each number in the range

# Take input
low, high = map(int, input('Enter the range: ').split())
for i in range(low, high + 1):
    for j in range(1, 5 + 1):
        print(i * j, end = ' ')
    print()