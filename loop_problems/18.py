# Count the frequency of each character in a string

s = input("Enter a string: ")

freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char, count in freq.items():
    print(char, ":", count)
