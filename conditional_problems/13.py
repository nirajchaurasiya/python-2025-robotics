# Determine the nature of the roots of a quadratic equation using discriminant.
import cmath

from math import sqrt


def find_nature_of_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    print(discriminant)
    print(cmath.sqrt(15))
    # print(sqrt(15))

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return f"Two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        # root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root1_a = (-b) / (2 * a)
        root1_b = sqrt(-discriminant) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return f"Two complex roots: ({root1_a}+{root1_b}j) and {root2}"


a, b, c = 1, -3, 2  # Coefficients of x^2 - 3x + 2 = 0
print(find_nature_of_roots(a, b, c))

a, b, c = 1, -4, 4  # Coefficients of x^2 - 4x + 4 = 0
print(find_nature_of_roots(a, b, c))

a, b, c = 1, 1, 1  # Coefficients of x^2 + x + 1 = 0
print(find_nature_of_roots(a, b, c))
