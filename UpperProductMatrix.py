n = int(input('Enter dimensions: '))
print(*map(lambda x: ' '.join(map(str, x)), [[0] * i + [int(input('Enter a number: ')) for j in range(n - i)] for i in range(n)]), sep = '\n')
