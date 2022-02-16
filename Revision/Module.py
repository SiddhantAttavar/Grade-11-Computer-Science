# Math
import math

print(math.pi)

print(math.e)

x = float(input('Enter no.: '))
print(math.sqrt(x))

x = float(input('Enter no.: '))
print(math.ceil(x))

x = float(input('Enter no.: '))
print(math.ceil(x))

x = float(input('Enter no.: '))
y = float(input('Enter no.: '))
print(math.pow(x, y))

x = float(input('Enter no.: '))
print(math.fabs(x))

x = float(input('Enter no.: '))
print(math.sin(x))

x = float(input('Enter no.: '))
print(math.cos(x))

x = float(input('Enter no.: '))
print(math.tan(x))

# Random
import random

print(random.random())

l = int(input('Enter left: '))
r = int(input('Enter left: '))
print(random.randint(l, r))

l = int(input('Enter left: '))
r = int(input('Enter left: '))
print(random.randrange(l, r))

# Statistics
import statistics

l = list(map(int, input('Enter no.s: ').split()))
print(statistics.mean(l))

l = list(map(int, input('Enter no.s: ').split()))
print(statistics.median(l))

l = list(map(int, input('Enter no.s: ').split()))
print(statistics.mode(l))


