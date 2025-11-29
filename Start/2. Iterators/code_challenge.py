# I am given multiple sets and am required to find the largest number in all of them

import itertools

show_expected_result = False
show_hints = False

def find_largest(numbers):
    # The fastest way to do this is to chain the lists and find the max
    return max(itertools.chain.from_iterable(numbers))

test_numbers = [
    [43, 2, 77, 48, 24, 9, 3, 65, 41, 42, 10, 75, 14, 69, 61],
    [20, 47, 69, 38, 2, 49, 76, 42, 81, 34, 10, 47, 76, 85, 81, 72],
    [92, 105, 25, 61, 75, 40, 87, 9, 52, 77, 0, 11, 25],
    [48, 74, 81, 71, 32, 82, 39, 74, 37, 72, 15],
    [8, 26, 12, 71, 5, 83, 75, 30, 34, 77]
]

result = find_largest(test_numbers)
print(f"The largest number is {result}")