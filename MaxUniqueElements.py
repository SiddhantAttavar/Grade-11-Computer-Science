d = {}
n = int(input('Enter no. of elements: '))
for _ in range(n):
    k = input('Enter key: ')
    a = list(map(int, input().split()))
    d[k] = a

res = -1
resMax = 0

for k, v in d.items():
    x = len(set(v))
    if res == -1 or x > resMax:
        res = k
        resMax = x

print(res)
