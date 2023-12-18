# --- Day 18: Lavaduct Lagoon ---
#
# https://adventofcode.com/2023/day/18

DIR = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

INSTR = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def calculate_area(trench):
    n = len(trench)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += trench[i][0] * trench[j][1]
        area -= trench[j][0] * trench[i][1]
    return abs(area) / 2


def parse_line(line, part2):
    if not part2:
        direction, steps, _ = line.split()
        steps = int(steps)
    else:
        _, _, instruction = line.split()
        instruction = instruction[2:-1]
        direction = INSTR[instruction[-1]]
        steps = int(instruction[:-1], 16)
    return direction, steps


def update_trench(trench, direction, steps):
    dy, dx = DIR[direction]
    y, x = trench[-1]
    new_y, new_x = y + dy * steps, x + dx * steps
    trench.append((new_y, new_x))


def dig_trench(data, part2=False):
    trench = [(0, 0)]
    length = 0

    for line in data:
        direction, steps = parse_line(line, part2)
        update_trench(trench, direction, steps)
        length += steps

    area = calculate_area(trench) - length // 2 + 1
    return length + int(area)


def main():
    with open("input.txt") as file:
        data = file.read().strip().splitlines()

    part1 = dig_trench(data)
    part2 = dig_trench(data, part2=True)

    # The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
    print("Part 1:", part1)

    # Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
