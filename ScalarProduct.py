n, m = map(int, input('Enter dimensions: ').split())
a = [list(map(int, input('Enter row: ').split())) for _ in range(n)]
x = int(input('Enter no.: '))
a = [[i * x for i in row] for row in a]
print(*map(lambda x: ' '.join(map(str, x)), a), sep = '\n')
