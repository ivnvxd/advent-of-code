# https://adventofcode.com/2023/day/1

import re

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part1 = []
for line in lines:
    values = [i for i in line if i.isdigit()]
    part1.append(int(values[0] + values[-1]))

# What is the sum of all of the calibration values?
print("Part 1:", sum(part1))

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

nums = list(str(i) for i in range(1, 10))
pattern = "(?=(" + "|".join(list(digits) + nums) + "))"

part2 = []
for line in lines:
    matches = re.findall(pattern, line)
    values = [digits.get(i, i) for i in matches]
    part2.append(int(values[0] + values[-1]))

# What is the sum of all of the calibration values?
print("Part 2:", sum(part2))
