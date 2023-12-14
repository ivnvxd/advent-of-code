# --- Day 18: Boiling Boulders ---
#
# https://adventofcode.com/2022/day/18

from collections import deque

DIRECTIONS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

data = [line.strip() for line in open("input")]

# Make a dict of all cube's position points as keys and uncovered side counts as values
cubes = {tuple(map(int, item.split(","))): 0 for item in data}

# Iterate through all cubes in dict
for cube in cubes.keys():
    # Iterate through all possible directions for the current cube
    for direction in DIRECTIONS:
        # Add an uncovered side count to the current cube if there is no other cube in current direction
        if tuple(x + y for x, y in zip(cube, direction)) not in cubes:
            cubes[cube] += 1

surface = sum(cubes.values())

# Clear the dict covered sides for the second part
cubes = {cube: 0 for cube in cubes}

# Find the minimum and maximum coordinate in each direction
min_ = tuple(min(x) - 1 for x in zip(*cubes))
max_ = tuple(max(x) + 1 for x in zip(*cubes))

check = deque([min_])
visited = set()

while len(check) > 0:
    # Take the first item, starting from the minimum coordinates
    coord = check.pop()

    # Check if we've already been in this point, add to the visited counter if not
    if coord in visited:
        continue
    visited.add(coord)

    # Iterate through all possible directions for the current coordinate
    for direction in DIRECTIONS:
        # Find the neighbor of the coordinate in current direction
        neighbor = tuple(x + y for x, y in zip(coord, direction))

        # Check if all of this neighbor's coordinates are between minimum and maximum coordinates
        if all(a <= b <= c for a, b, c in zip(min_, neighbor, max_)):
            # Check if the neighbour is actually a cube, that means it is the outer side of our lava droplet
            if neighbor in cubes:
                cubes[neighbor] += 1
            # Add to the list of points to check if not
            else:
                check.append(neighbor)

exterior = sum(cubes.values())

# What is the surface area of your scanned lava droplet?
print("Part 1:", surface)

# What is the exterior surface area of your scanned lava droplet?
print("Part 2:", exterior)
