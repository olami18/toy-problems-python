def consonant_value(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0
    for letter in word:
        if letter in consonants:
            current_value += ord(letter) - ord("a") + 1
            if current_value > max_value:
                max_value = current_value
        else:
            current_value = 0
    return max_value

print(consonant_value("zodiacs"))  # Output: 26
print(consonant_value("strength"))  # Output: 57
