# Determine if a person is a child, teenager, adult, or senior based on their age.
user_age = int(input("Enter your age: "))

if user_age < 13:
    print("You are still a child")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenager, boy!")
elif user_age >= 20 and user_age <= 59:
    print("You are an adult")
else:
    print("You are a senior")
