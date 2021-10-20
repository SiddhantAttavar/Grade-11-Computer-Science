# Create a list
l1 = [1, 'hello', ['abc', 'xyz', 'pqr'], [10, 20, 30]]

# Elements of the list
print(l1[0]) # 1
print(l1[1]) # hello
print(l1[2]) # ['abc', 'xyz', 'pqr']
print(l1[3]) # [10, 20, 30]

# Access elements from inner list
print(l1[2][0]) # abc

# Access elements from string in inner list
print(l1[2][0][0]) # a