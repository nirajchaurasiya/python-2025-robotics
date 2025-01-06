# Determine if an input character is a vowel, consonant, digit, or special character.
def character_type(char):

    vowels = "aeiouAEIOU"

    if char in vowels:

        return "Vowel"

    elif char.isdigit():

        return "Digit"

    elif char.isalpha() and char not in vowels:

        return "Consonant"

    else:

        return "Special Character"


print(character_type("a"))  # Output: Vowel

print(character_type("Z"))  # Output: Consonant

print(character_type("5"))  # Output: Digit

print(character_type("@"))  # Output: Special Character
