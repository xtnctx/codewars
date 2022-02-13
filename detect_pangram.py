"""

A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

"""

import string


def is_pangram(s):
    LOWER_CASE_ALPHABET = string.ascii_lowercase
    REQUIRED_POINTS = len(LOWER_CASE_ALPHABET)
    char_points = 0
    
    for letter in LOWER_CASE_ALPHABET:
        if letter in s.lower():
            char_points += 1
    
    if char_points == REQUIRED_POINTS:
        return True
    return False

text = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(text))