# Take three numbers as input and print the largest one.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(f"{a} is larger than {b} and {c}")

elif b > c:
    print(f"{b} is larger than {a} and {c}")

else:
    print(f"{c} is greater than {a} and {b}")
