# Lists
tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities[1])

print(tea_varities[-1])

print(tea_varities[1:3])

print(tea_varities[:2])

print(tea_varities[2:])

tea_varities[3] = "Herbal"

print(tea_varities)

print(tea_varities[1:2])

# tea_varities[1:2] = "Lemon"

# print(tea_varities)

tea_varities[1:2] = ["Lemon"]

print(tea_varities)

print(tea_varities[1:3])

tea_varities[1:3] = ["green", "masala"]

print(tea_varities)

print(tea_varities[1:1])

tea_varities[1:1] = ["test", "test"]

print(tea_varities)

print(tea_varities[1:3])

tea_varities[1:3] = []

print(tea_varities)


# tea_varities2 = ["Black", "green", "masala", "Herbal"]

# tea_varities2 = tea_varities

# print(tea_varities is tea_varities2)

for tea in tea_varities:
    print(tea, end="-")

tea_varities.append("Oolong")

if "Oolong" in tea_varities:
    print("I have Oolong tea")

# print(tea_varities)

# tea_varities.pop()

print(tea_varities)

tea_varities.remove("green")

print(tea_varities)

tea_varities.insert(1, "green")

print(tea_varities)

tea_varities_copy = tea_varities.copy()

print(tea_varities is tea_varities_copy)

squared_nums = [x**2 for x in range(10)]

print(squared_nums)

cube_numbers = [x**3 for x in range(10)]

print(cube_numbers)
