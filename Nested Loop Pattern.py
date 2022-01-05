# Print the following patterns
# Pattern 1:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 
# Pattern 2:
# A
# B C
# D E F
# G H I J

# Print pattern 1
x = 1
n = 4
for i in range(n):
	for j in range(i + 1):
		print(x, end = ' ')
		x += 1
	print()
print()

# Print pattern 2
x = ord('A')
for i in range(n):
    for j in range(i + 1):
        print(chr(x), end = ' ')
        x += 1
    print()
print()

# Single loop version
rowNum = 1
colNum = 0
for i in range(1, 11):
    colNum += 1
    if colNum == rowNum:
        print(i)
        colNum = 0
        rowNum += 1
    else:
        print(i, end = ' ')
