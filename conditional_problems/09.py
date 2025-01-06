# Take marks as input and assign grades (e.g., A, B, C) based on the score.

"""
A if grade is greater than 90
B if grade is greater than 80 and lesser than 90
C is lesser than 80
"""

grade = 80

if grade > 90:
    print("You got an A")
if grade > 80 and grade <= 90:
    print("You got a B")
else:
    print("You got C")
