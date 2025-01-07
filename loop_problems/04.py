# Generate the first \( n \) terms of the Fibonacci sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n = 10
a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b
