# Calculate the sum of the first \( n \) terms of the harmonic series

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
print("The sum of the first", n, "terms of the harmonic series is", sum)
