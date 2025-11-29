# Example file for Advanced Python by Joe Marini
# Sequence comparisons

import itertools


# define some lists
seq1 = [1, 2, 3, 4, 5, 6, 7]
seq2 = [100, 1, 1, 1, 1, 1, 1]

# define a tuple
seq3 = (1, 2, 3, 4, 5, 6, 7)

# compare the sequences
# print(seq1 == seq2)
# print(seq1 > seq2)
# print(seq1 < seq2)

# sequences that have equal values but different number of items:
# seq4 = [10, 20, 30]
# seq5 = [10, 20, 30, None, None]
# print(seq5 > seq4)

# Sequences must be of the same type to be compared
# print(seq1 > list(seq3))

# use the all() function to compare two arbitrary sequences
result = all(x == y for x, y in itertools.zip_longest(seq1, seq3))
print(result)