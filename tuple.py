# Immutable

tea_types = ("Black", "Green", "Oolong")

print(tea_types[0])

print(tea_types[1:3])

# tea_types[0] = "Lemon" => Not possible because of immutable

more_tea = ("Herbal", "Earl Grey")

print(more_tea)

all_tea = more_tea + tea_types

print(all_tea)

more_tea = ("Herbal", "Earl Gray", "Herbal")

print(more_tea)

if "Green" in all_tea:
    print("I have green tea")

print(more_tea.count("Herbal"))

print(more_tea.count("Herb"))

print(tea_types)

(black, green, Oolong) = tea_types

print(black)

print(green)

print(Oolong)

print(type(tea_types))

# ("",(1,2,3),"")
