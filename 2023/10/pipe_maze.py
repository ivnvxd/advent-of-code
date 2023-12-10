# https://adventofcode.com/2023/day/10

from collections import deque

FROM = {
    "north": "S|7F",
    "east": "S-J7",
    "south": "S|LJ",
    "west": "S-LF",
}

TO = {
    "north": "|7F",
    "east": "-J7",
    "south": "|LJ",
    "west": "-LF",
}

with open("input.txt") as file:
    data = file.read().strip().splitlines()

for row, line in enumerate(data):
    for col, char in enumerate(line):
        if char == "S":
            start = (row, col)
            break
    else:
        continue
    break

loop = set((start,))
queue = deque([start])

while queue:
    row, col = queue.popleft()
    cur = data[row][col]

    if (
        cur in FROM["south"]
        and data[row - 1][col] in TO["north"]
        and (row - 1, col) not in loop
    ):
        loop.add((row - 1, col))
        queue.append((row - 1, col))

    if (
        cur in FROM["west"]
        and data[row][col + 1] in TO["east"]
        and (row, col + 1) not in loop
    ):
        loop.add((row, col + 1))
        queue.append((row, col + 1))

    if (
        cur in FROM["north"]
        and data[row + 1][col] in TO["south"]
        and (row + 1, col) not in loop
    ):
        loop.add((row + 1, col))
        queue.append((row + 1, col))

    if (
        cur in FROM["east"]
        and data[row][col - 1] in TO["west"]
        and (row, col - 1) not in loop
    ):
        loop.add((row, col - 1))
        queue.append((row, col - 1))

part1 = len(loop) // 2

# How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
print("Part 1:", part1)
