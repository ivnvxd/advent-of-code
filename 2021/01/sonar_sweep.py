# --- Day 1: Sonar Sweep ---
#
# https://adventofcode.com/2021/day/1

sonar = [int(line.strip()) for line in open("input")]

increased = 0
sum_increased = 0

for i in range(len(sonar)):
    if i >= 1 and sonar[i] > sonar[i - 1]:
        increased += 1
    if (
        i >= 3
        and sonar[i] + sonar[i - 1] + sonar[i - 2]
        > sonar[i - 1] + sonar[i - 2] + sonar[i - 3]
    ):
        sum_increased += 1

# How many measurements are larger than the previous measurement?
print("Part 1:", increased)

# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
print("Part 2:", sum_increased)
