# Write Python programs to display the numbers of the given series along with their sum:
# a) 2/9 – 5/13 + 8/17 .... (upto 7 terms)
# b) 1^2 + 3^2 + 5^2 +...... + n^2 (input n)

# Series A
sumA = 0
for i in range(7):
    val = (2 + i * 3) / (9 + i * 4)
    sumA += val if i % 2 == 0 else val
    print(val, end = ' ')
print(f'\nSum of series A: {sumA}')

# Series B
sumB = 0
for i in range(1, 2 * int(input('Enter the number of terms of series B: ')), 2):
    sumB += i * i
    print(i * i, end = ' ')
print(f'\nSum of series B: {sumB}')
