# Write a program to print the following patterns based on choice - pattern a or 
# pattern b 
# 
# Pattern A:
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
# 
# Pattern B:
# Y
# X W
# V U T
# S R Q P

while True:
    # Take inpout
    choice = input('Enter A for pattern A, B for pattern B, or E for exit (A/B/E): ')
    if choice == 'A':
        # User selected pattern A
        for i in range(5):
            for j in range(i + 1):
                print((2 * i + 1) - 2 * j, end = ' ')
            print()
    elif choice == 'B':
        # User selected pattern B
        currChar = ord('Y')
        for i in range(4):
            for j in range(i + 1):
                print(chr(currChar), end = ' ')
                currChar -= 1
            print()
    else:
        # Exit the loop
        break

'''Output:
Enter A for pattern A, B for pattern B, or E for exit (A/B/E): A
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
Enter A for pattern A, B for pattern B, or E for exit (A/B/E): B
Y
X W
V U T
S R Q P
Enter A for pattern A, B for pattern B, or E for exit (A/B/E): E
'''