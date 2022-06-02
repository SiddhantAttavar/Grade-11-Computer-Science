l, r = map(int, input().split())
divisorSum = {i: 0 for i in range(l, r + 1)}

for i in range(1, r):
    if l % i == 0:
        divisorSum[l] += i
    for j in range(l + i - l % i, r + 1, i):
        divisorSum[j] += i

for num, divisorSum in divisorSum.items():
    if 2 * num == divisorSum:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')
