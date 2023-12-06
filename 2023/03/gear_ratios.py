# https://adventofcode.com/2023/day/3


def sum_parts(ranges, data):
    parts = []
    for y, x in ranges:
        part_num = ""
        while x < cols and data[y][x].isdigit():
            part_num += data[y][x]
            x += 1

        parts.append(int(part_num))

    return parts


with open("input.txt") as file:
    data = file.read().splitlines()

rows = len(data)
cols = len(data[0])
counted = set()
part2 = 0

for y in range(rows):
    for x in range(cols):
        symbol = data[y][x]
        if not symbol.isdigit() and symbol != ".":
            gears = set()
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny = y + dy
                    nx = x + dx
                    if (ny, nx) not in counted:
                        if 0 <= nx < cols and 0 <= ny < rows and data[ny][nx].isdigit():
                            while nx > 0 and data[ny][nx - 1].isdigit():
                                nx -= 1

                            counted.add((ny, nx))

                            if symbol == "*":
                                gears.add((ny, nx))

            if len(gears) == 2:
                parts = sum_parts(gears, data)
                gear_ratio = parts[0] * parts[1]
                part2 += gear_ratio

part1 = sum(sum_parts(counted, data))

# Part 1: What is the sum of all of the part numbers in the engine schematic?
print("Part 1:", part1)

# Part 2: What is the sum of all of the gear ratios in your engine schematic?
print("Part 2:", part2)
