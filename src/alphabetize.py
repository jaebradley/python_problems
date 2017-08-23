"""
Take a string and return all input characters in alphabetical order.
Assume that no numbers or punctuation will be used.
For the same character, uppercase characters should be returned before lowercase characters.
Do not use the `sorted` helper method.
Do not use any libraries that are not included with Python 3.6.1
"""


def alphabetize(value):
    uppercase_key = 'uppercase'
    lowercase_key = 'lowercase'

    character_counts = []
    for i in range(26):
        character_counts.append({uppercase_key: 0, lowercase_key: 0})

    for character in value:
        index = ord(character.lower()) - ord('a')
        counts = character_counts[index]
        key = uppercase_key if character.isupper() else lowercase_key

        counts[key] += 1

    alphabetized = []
    for index, counts in enumerate(character_counts):
        character = chr(ord('a') + index)
        uppercase_counts = counts[uppercase_key]
        lowercase_counts = counts[lowercase_key]
        for i in range(uppercase_counts):
            alphabetized.append(character.upper())
        for i in range(lowercase_counts):
            alphabetized.append(character)

    return ''.join(alphabetized)


