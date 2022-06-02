# Write a program to accept the age of n employees and count the number of persons in the following age group:
# Take input
n = int(input('Enter the number of students: '))

# Intialize age group counts
age26_35 = 0
age36_45 = 0
age46_55 = 0

# Take input
ages = list(map(int, input('Enter the age of the students: ').split()))

for age in ages:    
    # Increment the age
    if 26 <= age <= 35:
        age26_35 += 1
    elif 36 <= age <= 45:
        age36_45 += 1
    elif 46 <= age <= 55:
        age46_55 += 1

# Print the result
print(f'Age 26 to 35: {age26_35}')
print(f'Age 36 to 45: {age36_45}')
print(f'Age 26 to 35: {age46_55}')
