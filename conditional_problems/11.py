# Calculate BMI and print if the user is underweight, normal, overweight, or obese.
# underweight if their BMI is below 18.5, normal weight if their BMI is between 18.5 and 24.9, overweight if their BMI is between 25 and 29.9, and obese if their BMI is 30 or higher.

bmi = 24


def check_bmi(bmi):
    if bmi < 18.5:
        print("You are underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You are normal")
    elif bmi >= 25 and bmi <= 29.9:
        print("You are overweight")
    else:
        print("You are obese")


check_bmi(bmi)
