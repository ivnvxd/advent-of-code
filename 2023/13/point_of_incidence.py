# https://adventofcode.com/2023/day/13

import numpy as np


def mirror(lines, smudge=0):
    for line in range(1, len(lines)):
        above = lines[:line][::-1]
        below = lines[line:]

        trim = min(len(above), len(below))

        if (above[:trim] != below[:trim]).sum() == smudge:
            return line

    return 0


with open("input.txt") as file:
    data = file.read().strip()


part1, part2 = 0, 0
for pattern in data.split("\n\n"):
    lines = np.array([[*line] for line in pattern.splitlines()])

    part1 += mirror(lines) * 100 + mirror(lines.T)
    part2 += mirror(lines, 1) * 100 + mirror(lines.T, 1)


# What number do you get after summarizing all of your notes?
print("Part 1:", part1)

# What number do you get after summarizing the new reflection line in each pattern in your notes?
print("Part 2:", part2)
