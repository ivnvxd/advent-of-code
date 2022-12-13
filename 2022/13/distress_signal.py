# https://adventofcode.com/2022/day/13

from functools import cmp_to_key


def compare(first, second):
    # Check if inputs are integer
    first_is_int = isinstance(first, int)
    second_is_int = isinstance(second, int)

    # If both are integers
    if first_is_int and second_is_int:
        return first - second

    # If one of them is integer, wrap it and compare again
    elif first_is_int != second_is_int:
        if first_is_int:
            return compare([first], second)
        else:
            return compare(first, [second])

    # If both are lists, check them pairwise
    elif not first_is_int and not second_is_int:
        for a, b in zip(first, second):
            result = compare(a, b)
            if result != 0:
                return result

        # Compare length of equal lists
        return len(first) - len(second)


with open('input') as file:
    data = file.read().strip().split('\n\n')

indices = 0
packets = [[[2]], [[6]]]

for i, pair in enumerate(data):
    first, second = map(eval, pair.split('\n'))
    packets.append(first)
    packets.append(second)
    if compare(first, second) < 0:
        indices += i + 1

# Sort list of inputs using cmp_to_key functions
packets.sort(key=cmp_to_key(compare))
key = ((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))

# Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
print('Part 1:', indices)

# Organize all of the packets into the correct order. What is the decoder key for the distress signal?
print('Part 2:', key)
