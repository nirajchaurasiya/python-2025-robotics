# Check if a number has 1, 2, or more digits.
number_to_string = input("Enter number of any digit: ")

# number_to_string = str(number)

# length = len(number_to_string)

# print(length)

how_many_one = 0

how_many_two = 0

how_many_zero = 0

total_digit = 0

how_many_except_zero_one_two = 0

for x in range(len(number_to_string)):
    total_digit += 1
    if number_to_string[x] == str(0):
        how_many_zero += 1
    elif number_to_string[x] == str(1):
        how_many_one += 1
    elif number_to_string[x] == str(2):
        how_many_two += 1
    else:
        how_many_except_zero_one_two += 1

print(f"Total digit: {total_digit}")
print(f"0: {how_many_zero}")
print(f"1: {how_many_one}")
print(f"2: {how_many_two}")
print(f"Except 0, 1, 2: {how_many_except_zero_one_two}")
