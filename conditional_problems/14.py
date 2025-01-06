# Check if all digits of a number are odd.


def are_all_digits_odd(number):
    for digit in str(number):
        if int(digit) % 2 == 0:
            return False
    return True


# Example Usage
print(are_all_digits_odd(13579))  # Output: True
print(are_all_digits_odd(24689))  # Output: False
print(are_all_digits_odd(7))  # Output: True
