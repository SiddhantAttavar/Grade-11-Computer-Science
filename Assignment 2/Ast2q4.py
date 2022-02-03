'''
a) Accept names of 5 students along with their marks and store to a nested list Stu_Marks.
b) Display the original list in tabular format.
c)Search for a name (Which is taken as input) in the list and update the new mark which is input.
d)Display the updated list in tabular format.
e)Display a suitable message if the name doesn'texist in Stu_Marks.
List structure:[[name1, mark1], [name2, mark2],......]
'''

students = []
for i in range(5):
	students.append([input("Enter a name: "), int(input("Enter a mark: "))])

print("Original list: ")
print("Name\tMarks")
for i in students:
	print(i[0], '\t' , i[1])

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
