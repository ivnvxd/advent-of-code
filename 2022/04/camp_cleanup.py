# --- Day 4: Camp Cleanup ---
#
# https://adventofcode.com/2022/day/4

pairs = [line.strip() for line in open("input")]

contain = 0
overlap = 0

for item in pairs:
    first, second = item.split(",")

    start_1, end_1 = first.split("-")
    start_2, end_2 = second.split("-")
    start_1, end_1, start_2, end_2 = [int(x) for x in [start_1, end_1, start_2, end_2]]

    if start_1 <= start_2 and end_1 >= end_2 or start_1 >= start_2 and end_1 <= end_2:
        contain += 1

    if not (start_1 > end_2 or start_2 > end_1):
        overlap += 1

# In how many assignment pairs does one range fully contain the other?
print("Part 1:", contain)

# In how many assignment pairs do the ranges overlap?
print("Part 2:", overlap)
