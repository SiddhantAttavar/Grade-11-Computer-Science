# A computerized bus charges fare from each of its passengers based on the distance 
# travelled as per the tariff given below
# 
# Distance (in km)    Charges (in Rs.)
# First 10 kms        Rs. 50
# Next 15 kms         Rs. 4.5 / km
# More than 25 kms    Rs. 4 / km
# 
# As the passenger enters the bus, the computer prompts” Enter distance you intend 
# to travel (in km)”. On entering the distance, it prints the ticket and the control goes 
# back for the next passenger. At the end of journey, the computer prints the 
# following:
# a) The number of passengers travelled.
# b) Total fare received.
# Write a program to perform the above task. 

# Initialize number of passengers and total fare received
numPassengers = 0
totalFare = 0

while True:
    # Take input
    distance = float(input('Enter r distance you intend to travel (in km) or -1 to exit: '))
    
    # Check if the distance is 0 to exit
    if distance == -1:
        break

    # Calculate the cost
    cost = 50
    if distance > 25:
        # Add cost for next 15 kms and distance after that
        cost += 15 * 4.5
        cost += (distance - 25) * 4
    elif distance > 10:
        # Add cost for next 15 kms
        cost += (distance - 10) * 4.5

    # Print the result
    print('Your fare for this trip:', cost)

    # Add the cost to the total and increment the number of passengers
    numPassengers += 1
    totalFare += cost

# Print final result
print('Number of passengers travelled:', numPassengers)
print('Total fare received:', totalFare)

'''Output:
Enter r distance you intend to travel (in km) or -1 to exit: 5
Your fare for this trip: 50
Enter r distance you intend to travel (in km) or -1 to exit: 20
Your fare for this trip: 95.0
Enter r distance you intend to travel (in km) or -1 to exit: 40
Your fare for this trip: 177.5
Enter r distance you intend to travel (in km) or -1 to exit: -1
Number of passengers travelled: 3
Total fare received: 322.5
'''