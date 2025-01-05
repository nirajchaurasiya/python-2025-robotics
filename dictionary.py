chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types["Ginger"])

print(chai_types.get("Ginger"))

chai_types["Green"] = "Fresh"

print(chai_types)

for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("I have masala chai")

print(len(chai_types))

print(chai_types)

chai_types["Earl Grey"] = "Citrus"

print(chai_types)

chai_types.pop("Ginger")

print(chai_types)

chai_types.popitem()

print(chai_types)

del chai_types["Green"]

print(chai_types)

chai_types_copy = chai_types.copy()

print(chai_types_copy)

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"},
}

print(tea_shop)

print(tea_shop["Tea"]["Green"])

squared_nums = {x: x**2 for x in range(10)}

print(squared_nums)

squared_nums.clear()

print(squared_nums)

keys = ["Masala", "Ginger", "Lemon"]

print(keys)

default_values = "Delicious"

print(default_values)

new_dict = dict.fromkeys(keys, keys)

print(new_dict)
