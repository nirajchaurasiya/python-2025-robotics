# Check if a number is an Armstrong number

# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers

number = 154

number_str = input("Enter the number to check: ")

check_armstrong = 0

for i in range(len(number_str)):
    check_armstrong += int(number_str[i]) ** 3

if int(number_str) == check_armstrong:
    print(f"{int(number_str)} == {check_armstrong} Armstrong")
else:
    print(f"{int(number_str)} != {check_armstrong} Not armstrong")
