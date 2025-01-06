# Input a number (1–7) and display the corresponding day of the week.
# For automatic calendar ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

import calendar

# print(calendar)
# <module 'calendar' from '/usr/lib/python3.12/calendar.py'>

weekdays = list(calendar.day_name)
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

week_day = int(input("Enter from 1-7 starting from Mon-Sun: "))

if week_day > 0 and week_day <= 7:
    print(weekdays[week_day - 1])
else:
    print("Sorry, but only from 1 to 7 is available")
