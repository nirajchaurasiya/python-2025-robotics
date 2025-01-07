# Calculate the sum of squares of the first \( n \) natural numbers


n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):

    sum += i**2

print("The sum of squares of the first", n, "natural numbers is", sum)
