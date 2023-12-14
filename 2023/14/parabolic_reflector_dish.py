# --- Day 14: Parabolic Reflector Dish ---
#
# https://adventofcode.com/2023/day/14


import numpy as np


def tilt(grid):
    for y, x in np.argwhere(grid == "O"):
        grid[y, x] = "."
        while y > 0 and grid[y - 1, x] == ".":
            y -= 1
        grid[y, x] = "O"


def cycle(grid):
    for _ in range(4):
        tilt(grid)
        grid = np.rot90(grid, k=-1)


def weigh(grid):
    y, _ = np.nonzero(grid[::-1] == "O")
    return (y + 1).sum()


def main():
    with open("input.txt") as input:
        data = input.read().strip().splitlines()
        grid = np.array([[*line] for line in data])

    # Part 1
    tilt(grid)
    part1 = weigh(grid)

    # Part 2
    seen = {}
    iterations = 1000000000
    iter_count = 0
    cycle_length = None

    while iter_count < iterations:
        hash = grid.tobytes()
        if hash in seen:
            cycle_length = iter_count - seen[hash]
            break
        seen[hash] = iter_count

        cycle(grid)
        iter_count += 1

    if cycle_length is not None:
        remaining_iters = (iterations - iter_count) % cycle_length
        for _ in range(remaining_iters):
            cycle(grid)

    part2 = weigh(grid)

    # Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
    print("Part 1:", part1)

    # Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
