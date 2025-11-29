# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions

# For me: lambda can be equal to a normal function in this way:
# def test_function_1(var1, var2):
#     return var1 + var2
#
# test_function_2 = lambda var1, var2: var1 + var2
#
# print(test_function_1(1, 2) == test_function_1(1, 2))

# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions
# evensSquared = list(map(lambda x: x ** 2, filter(lambda e: 4 < e < 16, evens)))
# print(evensSquared)

# Derive a new list of numbers frm a given list
evensSquared = [e**2 for e in evens]
print(evensSquared)

# Limit the items operated on with a predicate condition
oddsSquared = [o**2 for o in odds if 3 < o < 17]
print(oddsSquared)