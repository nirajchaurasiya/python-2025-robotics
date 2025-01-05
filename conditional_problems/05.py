# # Determine if a year entered by the user is a leap year.
# def check_leap_year(y):
#     if (y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0):
#         return "Yes"
#     else:
#         return "No"


# # Driver code
# if __name__ == "__main__":
#     year = 2020
#     print(f"{year} is a leap year: {check_leap_year(year)}")


# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

year = 2024


def check_leap_year(year):
    # Step 1
    if year % 4 == 0:
        # Step 2
        if year % 100 == 0:
            # Step 3
            if year % 400 == 0:
                print("Is a leap year")
            else:
                print("Not a leap year")
        else:
            print("A leap year")
    else:
        # Step 5
        print("Not a leap year")


check_leap_year(year)
