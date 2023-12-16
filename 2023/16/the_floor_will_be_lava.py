# --- Day 16: The Floor Will Be Lava ---
#
# https://adventofcode.com/2023/day/16


def direction(cur, dy, dx):
    match cur:
        case "/":
            dy, dx = -dx, -dy
        case "\\":
            dy, dx = dx, dy
        case "|":
            dy, dx = 1, 0
        case "-":
            dy, dx = 0, 1

    return dy, dx


def traverse(data, m, n, start):
    stack = [start]
    seen = set()
    energized = set()

    while stack:
        y, x, dy, dx = stack.pop()
        if (y, x, dy, dx) in seen:
            continue
        seen.add((y, x, dy, dx))

        y += dy
        x += dx

        if not (0 <= y < m and 0 <= x < n):
            continue

        cur = data[y][x]

        if cur == "|":
            stack.append((y, x, -1, 0))
        elif cur == "-":
            stack.append((y, x, 0, -1))

        dy, dx = direction(cur, dy, dx)
        stack.append((y, x, dy, dx))
        energized.add((y, x))

    return len(energized)


def get_all_directions(m, n):
    directions = []

    for y in range(m):
        directions.append((y, -1, 0, 1))
        directions.append((y, m, 0, -1))
    for x in range(n):
        directions.append((-1, x, 1, 0))
        directions.append((n, x, -1, 0))

    return directions


def main():
    with open("input.txt") as input:
        data = input.read().strip().splitlines()

    m, n = len(data), len(data[0])

    start = (0, -1, 0, 1)
    part1 = traverse(data, m, n, start)

    directions = get_all_directions(m, n)
    part2 = max(traverse(data, m, n, start) for start in directions)

    # The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?
    print("Part 1:", part1)

    # Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
