# Find the sum of digits of a given number


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


n = int(input("Enter a number: "))
print("Sum of digits of", n, "is", sum_of_digits(n))
