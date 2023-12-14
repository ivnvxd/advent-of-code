# --- Day 9: Mirage Maintenance ---
#
# https://adventofcode.com/2023/day/9


def extrapolate(nums, part2=False):
    if all(n == 0 for n in nums):
        return 0

    diff = [y - x for x, y in zip(nums, nums[1:])]
    repeat = extrapolate(diff, part2)

    if not part2:
        extrapolation = nums[-1] + repeat
    else:
        extrapolation = nums[0] - repeat

    return extrapolation


with open("input.txt") as file:
    data = file.read()

part1, part2 = 0, 0

for line in data.splitlines():
    nums = list(map(int, line.split()))
    part1 += extrapolate(nums)
    part2 += extrapolate(nums, part2=True)


# Analyze your OASIS report and extrapolate the next value for each history. What is the sum of these extrapolated values?
print("Part 1:", part1)

# Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
print("Part 2:", part2)
