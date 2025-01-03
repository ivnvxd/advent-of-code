# --- Day 2: Red-Nosed Reports ---
#
# https://adventofcode.com/2024/day/2

def is_safe(levels):
    if len(levels) < 2:
        return True
    diffs = [levels[i] - levels[i-1] for i in range(1, len(levels))]
    increasing = diffs[0]
    return all(1 <= abs(d) <= 3 and (d > 0) == (increasing > 0) for d in diffs)

def is_safe_remove(levels):
    if is_safe(levels):
        return True
    return any(is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels)))

with open("input.txt") as file:
    data = file.read().splitlines()

part1 = part2 = 0

for report in data:
    levels = list(map(int, report.split()))
    part1 += is_safe(levels)
    part2 += is_safe_remove(levels)

print("Part 1:", part1)
print("Part 2:", part2)
