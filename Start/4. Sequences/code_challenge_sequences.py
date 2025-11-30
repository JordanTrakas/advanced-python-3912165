# I am given a unique set of characters and need to find a set of all the unique punctuation characters in the string

import string

def unique_characters(s):
    return {c for c in s if c in string.punctuation}

test_string = "The quick, brown fox: jumps over the lazy dog! Dog not amused."
print(unique_characters(test_string))