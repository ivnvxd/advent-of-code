# --- Day 12: Hot Springs ---
#
# https://adventofcode.com/2023/day/12

from functools import cache


def arrange(springs, nums):
    @cache
    def combinations(spring, num, acc):
        # Base cases for recursion (end of springs or nums)
        if num == len(nums):
            return springs.count("#", spring) == 0
        if spring == len(springs):
            return num == len(nums) - 1 and acc == nums[num]

        n = 0
        # If the current spring is not operational
        if springs[spring] != ".":
            n += combinations(spring + 1, num, acc + 1)

        # If the current spring is not damaged
        if springs[spring] != "#":
            if acc == nums[num]:
                n += combinations(spring + 1, num + 1, 0)
            elif acc == 0:
                n += combinations(spring + 1, num, 0)

        return n

    return combinations(0, 0, 0)


with open("input.txt") as file:
    data = file.read().strip().splitlines()

part1, part2 = 0, 0

for line in data:
    springs, records = line.split()
    nums = tuple(map(int, records.split(",")))
    part1 += arrange(springs, nums)

    springs2 = "?".join([springs] * 5)
    nums2 = nums * 5
    part2 += arrange(springs2, nums2)

# For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. What is the sum of those counts?
print("Part 1:", part1)

# Unfold your condition records; what is the new sum of possible arrangement counts?
print("Part 2:", part2)
