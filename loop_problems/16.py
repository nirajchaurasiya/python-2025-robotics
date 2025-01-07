# Convert a binary number to its decimal equivalent


def binary_to_decimal(n):
    decimal = 0
    base = 1
    while n > 0:
        decimal += n % 10 * base
        n = n // 10
        base = base * 2
    return decimal


n = int(input("Enter a binary number: "))

print("Decimal equivalent of", n, "is", binary_to_decimal(n))
