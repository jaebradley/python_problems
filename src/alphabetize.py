"""
Take a string and return all input characters in alphabetical order.
Assume that no numbers or punctuation will be used.
For the same character, uppercase characters should be returned before lowercase characters.
Do not use the `sorted` helper method.
"""


def alphabetize(string):
    uppercase_key = 'uppercase'
    lowercase_key = 'lowercase'

    character_counts = []
    for i in range(26):
        character_counts.append({uppercase_key: 0, lowercase_key: 0}.copy())

    for character in string:
        index = ord(character.lower()) - ord('a')
        counts = character_counts[index]
        key = uppercase_key if character.isupper() else lowercase_key

        count = counts[key]
        counts[key] = count + 1

    alphabetized_string = ''
    for index, counts in enumerate(character_counts):
        character = chr(ord('a') + index)
        uppercase_counts = counts[uppercase_key]
        lowercase_counts = counts[lowercase_key]
        for i in range(uppercase_counts):
            alphabetized_string += character.upper()
        for i in range(lowercase_counts):
            alphabetized_string += character

    return alphabetized_string


