# Convert Celsius to Fahrenheit or vice versa based on the user's choice.

# Celsius to Fahrenheit: (C × 9/5) + 32
# Fahrenheit to Celsius: (F − 32) x 5/9

print("1. Convert Celcius to Fahrenheit")
print("2. Convert Fahrenheit to Celcius")

user_choice = int(input("Enter your choice: "))

if user_choice == 1:
    # print("Enter the temperature in Celcius")
    fahrenheit = (float(input("Enter the temperature in Celcius: ")) * 9 / 5) + 32
    print(fahrenheit)
elif user_choice == 2:
    celcius = (float(input("Enter the temperature in Fahrenheit: ")) - 32) * 5 / 9
    print(celcius)
else:
    print("Invalid choice")
