# Check if a number is divisible by both 5 and 11.

number = int(input("Enter the number to check if its divisible by 5 or 11 or both: "))

if number % 5 == 0 and number % 11 == 0:
    print(f"{number} is divisible by both 5 and 11.")

elif number % 5 == 0:
    print(f"{number} is divisible by 5 only")

elif number % 11 == 0:
    print(f"{number} is divisible by 11 only")

else:
    print("The number is neither divisible by 5 or 11.")
