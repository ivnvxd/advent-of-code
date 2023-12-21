# --- Day 21: Step Counter ---
#
# https://adventofcode.com/2023/day/21
#
# TODO: Part 2

from collections import deque

DIR = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]


def find_start(grid):
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "S":
                return row, col
    return None


def calc_reach(grid, start, steps):
    m, n = len(grid), len(grid[0])

    plots = set()
    seen = {start}
    queue = deque([(start, steps)])

    while queue:
        (y, x), steps = queue.popleft()

        if steps % 2 == 0:
            plots.add((y, x))

        if steps == 0:
            continue

        for dy, dx in DIR:
            new_y, new_x = y + dy, x + dx
            if (
                0 <= new_y < m
                and 0 <= new_x < n
                and (new_y, new_x) not in seen
                and grid[new_y][new_x] != "#"
            ):
                seen.add((new_y, new_x))
                queue.append(((new_y, new_x), steps - 1))

    return len(plots)


def main():
    with open("input.txt") as file:
        grid = file.read().strip().splitlines()

    start = find_start(grid)
    part1 = calc_reach(grid, start, 64)

    # Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?
    print("Part 1:", part1)

    # However, the step count the Elf needs is much larger! Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?
    # print("Part 2:", part2)


if __name__ == "__main__":
    main()
