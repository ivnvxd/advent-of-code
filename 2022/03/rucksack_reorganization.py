# --- Day 3: Rucksack Reorganization ---
#
# https://adventofcode.com/2022/day/3


def count(letter):
    if letter.isupper():
        return ord(letter) - ord("A") + 1 + 26
    else:
        return ord(letter) - ord("a") + 1


rucksacks = [line.strip() for line in open("input")]

points = 0
group_points = 0

for item in rucksacks:
    first = item[: len(item) // 2]
    second = item[len(item) // 2 :]

    common = set(first).intersection(second)
    common = next(iter(common))

    # print(f'item: {item} — first: {first}, second: {second}, common: {common}')

    points += count(common)

i = 0

while i < len(rucksacks):
    first = rucksacks[i]
    second = rucksacks[i + 1]
    third = rucksacks[i + 2]

    common = set(first).intersection(second).intersection(third)
    common = next(iter(common))

    group_points += count(common)

    i += 3

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
print("Part 1:", points)

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
print("Part 2:", group_points)
