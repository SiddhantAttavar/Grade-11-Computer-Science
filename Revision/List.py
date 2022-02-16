# Creating
l1 = [1, 2, 3, 4, 5]

# Taking  input
l2 = []
n = int(input('Enter no. of elements: '))
for _ in range(n):
	l2.append(int(input('Enter no.: ')))

# Displaying
for i in l1:
	print(i, end = ' ')
print()

# Indexing
ind = int(input('Enter index: '))
print(l2[ind])

# Concatentation
l3 = l1 + l2
for i in l3:
	print(i, end = ' ')
print()

# Repetition
m = int(input('Enter multiple: '))
l4 = l1 * m
for i in l4:
	print(i, end = ' ')
print()

# Membership
x = int(input('Enter no.: '))
if x in l1:
	print('Yes')
else:
	print('No')

# Slicing
l = int(input('Enter left: '))
r = int(input('Enter right: '))
print(l1[l: r + 1])

# Traversing
for i in l1:
	print(i, end = ' ')
print()

# len()
print(len(l1))

# list()
l5 = list(map(int, input('Enter no.s: ').split()))

# append()
x = int(input('Enter no.: '))
l1.append(x)

# extend()
l1.extend(l2)

# insert()
x = int(input('Enter no.: '))
l1.insert(0, x)

# count()
x = int(input('Enter no.: '))
print(l1.count(x))

# index()
x = int(input('Enter no.: '))
print(l1.index(x))

# remove()
x = int(input('Enter no.: '))
l1.remove(x)

# pop()
i = int(input('Enter index: '))
l1.pop(i)

# reverse()
l1.reverse()

# sort()
l1.sort()

# sorted()
l6 = sorted(l2)

# min()
print(min(l1))

# max()
print(max(l1))

# sum()
print(sum(l1))

# Nested lists
l7 = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8]
]

# Find maximum
m = l1[0]
for i in range(1, len(l1)):
	if l1[i] > m:
		m = l1[i]
print(m)

# Find minimum
m = l1[0]
for i in range(1, len(l1)):
	if l1[i] < m:
		m = l1[i]
print(m)

# Find mean
s = 0
for i in l1:
	s += i
print(s / len(l1))

# linear search
x = int(input('Enter no.: '))
for i in range(i, 0, len(l1)):
	if l1[i] == x:
		print(i)
		break
else:
	print('Not found')

# Count freuency
f = {}
for i in l:
	if i in f:
		f[i] += 1
	else:
		f[i] = 1
