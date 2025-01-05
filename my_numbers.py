import random
import math


l1 = ["lemon", "masala", "ginger", "mint"]


def get_random_number():
    print(random.randint(1, 10))
    print(random.choice(l1))
    random.shuffle(l1)
    print(l1)


def truncat():
    # Goes towards 0
    print("-4.5", math.trunc(-4.5))
    print("4.5", math.trunc(4.5))


def floor_number():
    # Goes towards the base number
    print("-4.5", math.floor(-4.5))
    print("4.5", math.floor(4.5))


# print("Truncat")
# truncat()
# print("Floor")
# floor_number()


a = 0o20  # Octal because of o
b = 0xFF  # Hex because of x
c = 0b1000  # Binary because of b

# print(oct(64))
# print(bin(64))
# print(hex(64))

# print(int(3.14))

# print(int("64", 8))
# print(int("64", 16))
# print(int("1001", 2))
# print(int("64", 10))


# Bitwise operators

x = 1

# print(x << 2)
# Random

# get_random_number()

# print(Decimal("0.1 + 0.1 + 0.1 - 0.3"))


# from decimal import Decimal

# print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))

from fractions import Fraction

myFra = Fraction(2, 7)

print(myFra)

setone = {1, 2, 3, 4}

print(setone | {1, 3})
