# --- Day 3: Binary Diagnostic ---
#
# https://adventofcode.com/2021/day/3

from copy import deepcopy


def most_common_bit(data, pos, default):
    # Generate a list containing only items in current position
    common = list(map(int, [x[pos] for x in data]))

    # Count most common bit in position
    if common.count(0) < common.count(1):
        return 1
    elif common.count(0) > common.count(1):
        return 0

    # Return 0 or 1 if there are equal amount of bits in the position
    else:
        if default == 1:
            return default
        else:
            return 1 - default


def delete(data, pos, default):
    # Search for most or least common value
    if default == 1:
        check = most_common_bit(data, pos, default)
    else:
        check = 1 - most_common_bit(data, pos, default)

    # Generate new list containing only items with most or least common value in position
    new_data = [line for l, line in enumerate(data) if int(data[l][pos]) == check]

    # Check if list is not empty
    if len(new_data) != 0:
        return new_data
    else:
        return data


report = [line.strip() for line in open("input")]

length = len(report[0])
gamma_rate = ""
epsilon_rate = ""
oxygen = deepcopy(report)
co2 = deepcopy(report)

for i in range(length):
    gamma = most_common_bit(report, i, 1)
    epsilon = 1 - gamma
    gamma_rate += str(gamma)
    epsilon_rate += str(epsilon)

    oxygen = delete(oxygen, i, 1)
    co2 = delete(co2, i, 0)

gamma_rate = int(gamma_rate, base=2)
epsilon_rate = int(epsilon_rate, base=2)

oxygen_rate = int(oxygen[0], base=2)
co2_rate = int(co2[0], base=2)

# What is the power consumption of the submarine?
print("Part 1:", gamma_rate * epsilon_rate)

# What is the life support rating of the submarine?
print("Part 2:", oxygen_rate * co2_rate)
