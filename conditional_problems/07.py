# The sum of any two sides of a triangle must be greater than the third side.
# a+b>c
# a+c>b
# b+c>a

# It means the sum of two sides should always greater than the third one.

a = 1
b = 2
c = 10

if a + b > c and b + c > a and a + c > b:
    print("A valid triangle")
else:
    print("Not a valid triangle")
