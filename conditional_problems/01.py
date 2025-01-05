# Age group categorization
## Classify a person's age group: Child(< 13), Teenager (13-19), Adult (20-59), Senior (60+)

user_age = int(input("Enter your age: "))

if user_age < 13:
    print("You are still a child")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenager, boy!")
elif user_age >= 20 and user_age <= 59:
    print("You are an adult")
else:
    print("You are a senior")
