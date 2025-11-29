# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# a slice is a subset of a sequence. The form is [start:stop:step]
# print(names[1:4])

# using a step 
# print(names[0:7:2])

# shorthand
# print(names[:3])
# print(names[2:])

# reversing with step of -1
# print(names[::-1])
# print(names[::])

# assigning sequences
# new_names = ["Andy", "Stanley", "Angela"]
# names[2:5] = new_names
# print(names)

# the del operator works with slices
# del names[1::-1]
# print(names)

# not all sequence types support slicing, however
# deque_names = deque(["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"])
# for name in deque_names:
#     print(name, " ", end="")
# print(len(deque_names))
# print(deque_names[1:4]) # This raises a TypeError