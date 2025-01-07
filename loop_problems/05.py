# Reverse the digits of a given number

number = 123456789

number_str = str(number)

rev_str = ""

for i in range(len(number_str)):
    rev_str += number_str[-i - 1]

print(rev_str)
