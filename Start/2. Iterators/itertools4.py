# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools
import pprint

# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(cards, suits))
# print(len(deck))
# print(deck)

# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")
games = list(itertools.permutations(teams,2))
# print(games)

# combinations() will create combinations of a given length with no repeats
result = list(itertools.combinations("ABCD", 3))
# print(f"Result ({len(result)} items): {result}")

# combinations_with_replacement() will create combinations of a given length with repeats
combs_with_replacement = list(itertools.combinations_with_replacement("ABCD", 3))
len_combs_with_replacement = len(combs_with_replacement)
pprint.pp(combs_with_replacement)
print(f"Number of combinations: {len_combs_with_replacement}")
