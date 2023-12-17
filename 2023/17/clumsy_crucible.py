# --- Day 17: Clumsy Crucible ---
#
# https://adventofcode.com/2023/day/17

from heapq import heappop, heappush


def add_to_heap(heap, seen, heatloss, y, x, dy, dx, steps, data, m, n):
    new_y, new_x = y + dy, x + dx
    if 0 <= new_y < m and 0 <= new_x < n and (new_y, new_x, dy, dx, steps) not in seen:
        new_hl = heatloss + data[new_y][new_x]
        heappush(heap, (new_hl, new_y, new_x, dy, dx, steps))


def continue_same_direction(
    heap, seen, heatloss, y, x, dy, dx, steps, grid, m, n, max_steps
):
    if steps < max_steps and (dy, dx) != (0, 0):
        add_to_heap(heap, seen, heatloss, y, x, dy, dx, steps + 1, grid, m, n)


def explore_new_directions(
    heap, seen, heatloss, y, x, dy, dx, steps, grid, m, n, min_steps
):
    if steps >= min_steps or (dy, dx) == (0, 0):
        for new_dy, new_dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (new_dy, new_dx) != (dy, dx) and (new_dy, new_dx) != (-dy, -dx):
                add_to_heap(heap, seen, heatloss, y, x, new_dy, new_dx, 1, grid, m, n)


def traverse(grid, min_steps, max_steps):
    m, n = len(grid), len(grid[0])
    heap = [(0, 0, 0, 0, 0, 0)]
    seen = set()

    while heap:
        heatloss, y, x, dy, dx, steps = heappop(heap)

        if y == m - 1 and x == n - 1 and steps >= min_steps:
            break

        if (y, x, dy, dx, steps) in seen:
            continue

        seen.add((y, x, dy, dx, steps))

        continue_same_direction(
            heap, seen, heatloss, y, x, dy, dx, steps, grid, m, n, max_steps
        )
        explore_new_directions(
            heap, seen, heatloss, y, x, dy, dx, steps, grid, m, n, min_steps
        )

    return heatloss


def main():
    with open("input.txt") as file:
        grid = [list(map(int, line)) for line in file.read().strip().splitlines()]

    part1 = traverse(grid, 0, 3)
    part2 = traverse(grid, 4, 10)

    # Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?
    print("Part 1:", part1)

    # Directing the ultra crucible from the lava pool to the machine parts factory, what is the least heat loss it can incur?
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
