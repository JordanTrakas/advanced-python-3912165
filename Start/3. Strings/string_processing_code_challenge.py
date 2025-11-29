# The task is to create a dictionary from a string with the following format:
"""
{
    "Punctuation": (int),
    "Whitespace": (int),
    "Uppercase": (int),
    "Lowercase": (int),
    "Found": (bool), -> regardless of case
    "Index": (int) -> regardless of case
}"""

import string

def process_string(the_string, term):
    string_dict = {"Punctuation": 0,
                   "Whitespace": 0,
                   "Uppercase": 0,
                   "Lowercase": 0,
                   "Found": False,
                   "Index": -1}
    for char in the_string:
        if char in string.punctuation:
            string_dict["Punctuation"] += 1
        elif char in string.whitespace:
            string_dict["Whitespace"] += 1
        elif char in string.ascii_uppercase:
            string_dict["Uppercase"] += 1
        elif char in string.ascii_lowercase:
            string_dict["Lowercase"] += 1

    term_lowercase = term.lower()
    if the_string.find(term_lowercase) != -1:
        string_dict["Found"] = True
        string_dict["Index"] = the_string.index(term_lowercase)

    return string_dict

some_string = "The quick, brown 'fox' jumps OVER the lazy dog; dog not impressed!"
string_term = "Fox"

some_string_stats = process_string(some_string, string_term)
print(some_string_stats)