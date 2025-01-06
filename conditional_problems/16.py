# Check if the given dimensions form a rectangle or square.

a, b, c, d = 4, 5, 6, 7

if a == b == c == d:
    print("This creates a square")
elif a == c and b == d:
    print("This creates a rectangle")
else:
    print("Neither a rectangle nor a square")
