# Creating
t1 = (1, 2, 3, 4, 5)

# Taking  input
t2 = []
n = int(input('Enter no. of elements: '))
for _ in range(n):
	t2.append(int(input('Enter no.: ')))
t2 = tuple(t2)

# Displaying
for i in t1:
	print(i, end = ' ')
print()

# Indexing
ind = int(input('Enter index: '))
print(t2[ind])

# Concatentation
t3 = t1 + t2
for i in t3:
	print(i, end = ' ')
print()

# Repetition
m = int(input('Enter multiple: '))
t4 = t1 * m
for i in t4:
	print(i, end = ' ')
print()

# Membership
x = int(input('Enter no.: '))
if x in t1:
	print('Yes')
else:
	print('No')

# Slicing
l = int(input('Enter left: '))
r = int(input('Enter right: '))
print(t1[l: r + 1])

# Traversing
for i in t1:
	print(i, end = ' ')
print()

# len()
print(len(t1))

# tuple()
t5 = tuple(map(int, input('Enter no.s: ').split()))

# count()
x = int(input('Enter no.: '))
print(t1.count(x))

# index()
x = int(input('Enter no.: '))
print(l1.index(x))

# sorted()
l = sorted(t2)

# min()
print(min(t1))

# max()
print(max(t1))

# sum()
print(sum(t1))

# Nested lists
t6 = (
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8)
)

# Find maximum
m = t1[0]
for i in range(1, len(t1)):
	if t1[i] > m:
		m = t1[i]
print(m)

# Find minimum
m = t1[0]
for i in range(1, len(t1)):
	if t1[i] < m:
		m = t1[i]
print(m)

# Find mean
s = 0
for i in t1:
	s += i
print(s / len(t1))

# linear search
x = int(input('Enter no.: '))
for i in range(i, 0, len(t1)):
	if t1[i] == x:
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
