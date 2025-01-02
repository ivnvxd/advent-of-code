# --- Day 1: Historian Hysteria ---
#
# https://adventofcode.com/2024/day/1

with open("input.txt") as file:
    data = file.read().splitlines()

left = []
right = []
part1 = part2 = 0

for line in data:
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

for l, r in zip(left, right):
	part1 += abs(l - r)
	part2 += l * right.count(l)

# What is the total distance between your lists?
print("Part 1:", part1)

# What is their similarity score?
print("Part 2:", part2)
