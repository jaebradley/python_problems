# Problem

> * Take a string and return all input characters in alphabetical order
* Assume that no numbers or punctuation will be used
* For the same character, uppercase characters should be returned before lowercase characters
* Do not use the `sorted` helper method
* Do not use any libraries that are not included with Python 3.6.1

For example, `alphabetize(HelLo)` should return `eHLlo`

# Approach

1. Create a 26-element list. This list will represent the counts (uppercase 
   and lowercase) of the different alphabetical characters seen via a dictionary
2. Iterate through the characters in the input string
    1. Get the index for each character by subtracting the `int` values 
       of the lowercase character from the `int` value of `a`
    2. Get the existing count for that index & case from the counts 
       dictionary
    3. Increment the count by `1`
3. Initialize the return string
4. Iterate through each element in the list
    1. For each dictionary / element, get the character, and get the
       uppercase and lowercase counts
    2. Add the uppercase characters to the return string
    3. Add the lowercase characters to the return string
5. Return the alphabetized string

# Implementation Discussion

I know the 'Pythonic' way to accomplish this is something like 
`''.join(sorted(myString))`.

However, as somebody trying to learn Python, I wanted to use this exercise
to learn more about strings and characters in Python (for example) 
vs. Googling a one-liner (not that there's anything wrong with that).

Things I'm concerned about:

* Should this be a class? Or is it ok as a standalone method? (As 
  somebody that is more comfortable in Java, things that aren't in classes
  make me irrationally uneasy.)
* Speaking of which, there's a decent amount of stuff going on in this 
  method, should I break it up? 
  * If I decide to break it up, what's the right way of 'showing' that 
    some functions are only going to be used by another function? 
  * I think Python doesn't really have a concept of `private` vs. 
    `public` so do I `_(some_method_name)` here?
* What other 'Pythonic' elements am I missing (again, aside from using 
  the `sorted` method)?
    

# Implementation

<!-- language:lang-python -->
    
    def alphabetize(value):
        uppercase_key = 'uppercase'
        lowercase_key = 'lowercase'
    
        character_counts = []
        for i in range(26):
            character_counts.append({uppercase_key: 0, lowercase_key: 0}.copy())
    
        for character in value:
            index = ord(character.lower()) - ord('a')
            counts = character_counts[index]
            key = uppercase_key if character.isupper() else lowercase_key
    
            count = counts[key]
            counts[key] = count + 1
    
        alphabetized = ''
        for index, counts in enumerate(character_counts):
            character = chr(ord('a') + index)
            uppercase_counts = counts[uppercase_key]
            lowercase_counts = counts[lowercase_key]
            for i in range(uppercase_counts):
                alphabetized += character.upper()
            for i in range(lowercase_counts):
                alphabetized += character
    
        return alphabetized