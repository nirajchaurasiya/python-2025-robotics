# Print all prime numbers between 1 and \( n \)

n = int(input("Enter a number: "))

for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
