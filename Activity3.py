n = int(input('Enter no. of rows: '))
m = int(input('Enter no. of columns: '))

a = []
for i in range(n):
    r = []
    for j in range(m):
        r.append(int(input('Enter matrix element: ')))
    a.append(r)

b = []
for i in range(n):
    r = []
    for j in range(m):
        r.append(int(input('Enter matrix element: ')))
    b.append(r)

print('A: ')
for row in a:
    for i in row:
        print(i, end = ' ')
    print()

print()
print('B: ')
for row in b:
    for i in row:
        print(i, end = ' ')
    print()

