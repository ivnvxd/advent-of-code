# https://adventofcode.com/2023/day/8

import math

with open("input.txt") as file:
    data = file.read().strip()

steps, _, *instructions = data.splitlines()

graph = {}

for line in instructions:
    position, neighbors = line.split(" = ")
    neighbors = neighbors[1:-1]
    graph[position] = neighbors.split(", ")

# Part 1
node = "AAA"
step = 0
part1 = 0

while node != "ZZZ":
    if step == len(steps):
        step = 0

    if steps[step] == "L":
        node = graph[node][0]
    else:
        node = graph[node][1]

    step += 1
    part1 += 1

# Part 2
nodes = [key for key in graph.keys() if key.endswith("A")]
cycles = []

for node in nodes:
    step = 0
    cycle = -1
    prev = ""

    while not prev.endswith("Z"):
        if step == len(steps):
            step = 0

        if steps[step] == "L":
            prev, node = node, graph[node][0]
        elif steps[step] == "R":
            prev, node = node, graph[node][1]

        step += 1
        cycle += 1

    cycles.append(cycle)

part2 = math.lcm(*cycles)

# How many steps are required to reach ZZZ?
print("Part 1:", part1)

# How many steps does it take before you're only on nodes that end with Z?
print("Part 2:", part2)
