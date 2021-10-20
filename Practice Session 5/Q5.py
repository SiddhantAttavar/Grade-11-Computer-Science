# A shop charges Rs 150 per item if you buy less than 10 items. 
# If you buy between 10 and 99 items, the cost is Rs 120 per item. 
# If you buy 100 or more items, the cost is Rs 90 per item, 
# Write a program that takes the number of items bought, from the user and prints the total cost.  

# Take input
numItems = int(input('Enter the number of items: '))

# Calculate the total cost based on the number of items
if numItems < 0:
    print('Invalid input')
elif numItems < 10:
    print(f'The total cost is Rs. {numItems * 150}')
elif numItems < 100:
    print(f'The total cost is Rs. {numItems * 120}')
else:
    print(f'The total cost is Rs. {numItems * 90}')