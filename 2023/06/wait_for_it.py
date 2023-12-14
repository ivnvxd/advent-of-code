# --- Day 6: Wait For It ---
#
# https://adventofcode.com/2023/day/6

with open("input.txt") as file:
    data = file.read().strip()

lines = data.split("\n")

# Part 1
times, distances = [list(map(int, line.split(":")[1].split())) for line in lines]

part1 = 1
for time, distance in zip(times, distances):
    beat = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            beat += 1

    part1 *= beat

# Part 2
time2, distance2 = map(int, ("".join(line.split(":")[1].split()) for line in lines))

part2 = 1
beat2 = 0
for hold in range(time2):
    if hold * (time2 - hold) > distance2:
        beat2 += 1

part2 *= beat2

# Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?
print("Part 1:", part1)

# How many ways can you beat the record in this one much longer race?
print("Part 2:", part2)
