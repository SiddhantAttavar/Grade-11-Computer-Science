'''
This program Accept names of 5 students along with their marks, stores them to a nested list and performs operations:
 - Display the original list in tabular format
 - Search for a name and update the new mark
 - Display the updated list in tabular format
 - Display a suitable message if the name doesn't exist in Stu_Marks.
'''

# Take input
students = []
for i in range(5):
	students.append([input("Enter a name: "), int(input("Enter a mark: "))])

# Print original list
print("Original list: ")
print("Name\tMarks")
for i in students:
	print(i[0], '\t' , i[1])

# Update marks
name = input("Enter a name: ")
for i in students:
	if i[0] == name:
		i[1] = int(input("Enter a new mark: "))
		break
else:
	print("Name not found.")

'''Output:
Enter a name: Name1
Enter a mark: 100
Enter a name: Name2
Enter a mark: 90    
Enter a name: Name3
Enter a mark: 95    
Enter a name: Name4
Enter a mark: 97    
Enter a name: Name5
Enter a mark: 86
Original list: 
Name1 100
Name2 90
Name3 95
Name4 97
Name5 86
Enter a name: Name1
Enter a new mark: 79
'''
