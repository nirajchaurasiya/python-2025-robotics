# Count how many times each digit appears in a number.

n = int(input("Enter a number: "))

for i in range(10):
    count = 0
    temp = n
    while temp > 0:
        if temp % 10 == i:
            count += 1
        temp = temp // 10
    if count > 0:
        print(f"{i} appears {count} times")
