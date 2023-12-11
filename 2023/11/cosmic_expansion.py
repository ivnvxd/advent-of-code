# https://adventofcode.com/2023/day/11

with open("input.txt") as file:
    data = file.read().strip().splitlines()

empty_rows = [y for y, row in enumerate(data) if all(char == "." for char in row)]
empty_cols = [x for x, col in enumerate(zip(*data)) if all(char == "." for char in col)]

galaxies = [
    (y, x) for y, row in enumerate(data) for x, char in enumerate(row) if char == "#"
]

part1, part2 = 0, 0
for i, (y1, x1) in enumerate(galaxies):
    for y2, x2 in galaxies[i + 1 :]:
        distance = abs(y1 - y2) + abs(x1 - x2)

        part1 += distance
        part2 += distance

        for row in empty_rows:
            if y1 < row < y2 or y2 < row < y1:
                part1 += 1
                part2 += 999999

        for col in empty_cols:
            if x1 < col < x2 or x2 < col < x1:
                part1 += 1
                part2 += 999999

# What is the sum of these lengths?
print("Part 1:", part1)

# What is the sum of these lengths?
print("Part 2:", part2)
