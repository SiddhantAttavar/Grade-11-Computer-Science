# Creating
d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# Taking input
d2 = {}
n = int(input('Enter no. of elements: '))
for _ in range(n):
	k = int(input('Enter key: '))
	x = int(input('Enter no.: '))
	d2[k] = v

# Accessing using key
k = int(input('Enter key: '))
print(d1[k])

# Adding item
k = int(input('Enter key: '))
x = int(input('Enter no.: '))
d1[k] = v

# Modifying value
k = int(input('Enter key: '))
x = int(input('Enter no.: '))
d1[k] = v

# Traversing a dictionary
for k in d1:
	print(k, d1[v])

# len()
print(len(d1))

# dict()
l1 = [(int(input('Enter key: ')), int(input('Enter value: '))) for _ in range(int(input('Enter no. of elements: ')))]
d3 = dict(l)

# keys()
for k in d1.keys():
	print(k, d1[v])

# items()()
for k, v in d1.items()():
	print(k, v)

# get()
k = int(input('Enter key: '))
x = int(input('Enter no.: '))
print(d1.get(k, v))

# update()
d1.update(d2)

# del
k = int(input('Enter key: '))
del d[k]

# clear()
d1.clear()

# fromkeys()
k = list(map(int, input('Enter keys: ').split()))
x = int(input('Enter no.: '))
d4 = dict.fromkeys(k, v)

# copy()
d5 = dict.copy(d2)

# pop()
k = int(input('Enter key: '))
d2.pop(k)

# popitem()
x = int(input('Enter no.: '))
d2.pop(x)

# setdefault()
k = int(input('Enter key: '))
x = int(input('Enter no.: '))
print(d1.setdefault(k, v))

# max()
print(max(d2))

# min()
print(min(d2))

# count()
x = int(input('Enter no.: '))
print(d2.count(x))

# sorted()
l2 = sorted(d2)

# Count occurences of character
f = {}
s = input('Enter string: ')
for c in s:
	if c in f:
		f[c] += 1
	else:
		f[c] = 1

# Dictionary of employee salaries
e = {}
n = int(input('Enter no.: of elements: '))
for _ in range(n):
	n = input('Enter name: ')
	s = int(input('Enter salary: '))
	e[n] = s
n = input('Enter name: ')
print(e[n])
