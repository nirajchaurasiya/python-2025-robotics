# Check if a number is a palindrome


def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return temp == rev


n = int(input("Enter a number: "))
if is_palindrome(n):
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
