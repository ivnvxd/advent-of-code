# https://adventofcode.com/2023/day/2

with open("input.txt") as file:
    lines = [line.strip() for line in file]

pre_reqs = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

part1, part2 = 0, 0

for line in lines:
    pass_reqs = []
    min_reqs = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    power = 1

    game = line.split(": ")
    game_num = int(game[0].split(" ")[1])

    sets = game[1].split("; ")
    for s in sets:
        cubes = s.split(", ")
        for c in cubes:
            cube = c.split(" ")
            cube_color = cube[1]
            cube_count = int(cube[0])

            if cube_count > pre_reqs[cube_color]:
                pass_reqs.append(False)
            else:
                pass_reqs.append(True)

            min_reqs[cube_color] = max(min_reqs[cube_color], cube_count)

    if all(pass_reqs):
        part1 += game_num

    for v in min_reqs.values():
        power *= v

    part2 += power

# What is the sum of the IDs of those games?
print("Part 1:", part1)

# What is the sum of the power of these sets?
print("Part 2:", part2)
