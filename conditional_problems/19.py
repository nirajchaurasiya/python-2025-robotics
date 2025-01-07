# Verify if a given string is a palindrome.

# Way 1
# def check_palindrome(word):
#     word = word.replace(" ", "")
#     total_len = len(word)
#     str1 = [word[x].lower() for x in range(total_len)]
#     rev_str = []
#     # print(str1, len(str1), total_len)
#     for i in range(total_len):
#         # print(i)
#         rev_str.append(str1[total_len - (i + 1)])
#     print(str1)
#     print(rev_str)
#     count = 0
#     for i in range(total_len):
#         if str1[i] == rev_str[i]:
#             continue
#         else:
#             count += 1
#             break
#     if count:
#         print("Not palindrome")
#     else:
#         print("Palindrome")


# check_palindrome("I am a boy")
# aVaB = B is 4-1, a is 4-2, V is 4-3, a is 4-4


# Way 2


def check_palindrome(word):
    word = word.replace(" ", "").lower()
    print(word[::-1])
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


# Test cases
check_palindrome("I am a boy")  # Output: Not a palindrome
check_palindrome("A man a plan a canal Panama")  # Output: Palindrome
