# --- Day 14: Regolith Reservoir ---
#
# https://adventofcode.com/2022/day/14


def pour(sand, bottom, void=True):
    x, y = 500, 0

    # Check if there is endless void under the last rock
    if void:
        floor = bottom + 2
    else:
        floor = bottom

    # Calculate for one sand unit
    while y < bottom:
        # If there is nothing directly under the falling sand
        if (x, y + 1) not in rock and y + 1 < floor:
            y = y + 1

        # If there is an empty space one step down and to the left
        elif (x - 1, y + 1) not in rock and y + 1 < floor:
            x = x - 1
            y = y + 1

        # If there is an empty space one step down and to the right
        elif (x + 1, y + 1) not in rock and y + 1 < floor:
            x = x + 1
            y = y + 1

        # If all the possible destinations are blocked
        else:
            rock.add((x, y))
            sand += 1
            break

    return y, sand


data = [line.strip() for line in open("input")]

rock = set()

# Draw the cave and add all rocks
for line in data:
    # Split points
    points = line.split(" -> ")

    start = None

    for point in points:
        # Split coordinates
        x, y = point.split(",")
        x, y = int(x), int(y)

        # Do nothing for the first point in each line
        if start:
            # Count deltas between first and second point's coordinates
            dx = x - start[0]
            dy = y - start[1]

            # Move horizontally and add point to the rock
            if abs(dx) > abs(dy):
                for i in range(abs(dx) + 1):
                    rock.add((start[0] + i * (1 if dx > 0 else -1), y))
            # Move vertically
            else:
                for i in range(abs(dy) + 1):
                    rock.add((x, start[1] + i * (1 if dy > 0 else -1)))

        # Define the starting point
        start = (x, y)

# Calculate the depth of the cave
abyss = max(rock, key=lambda r: r[1])[1]

sand = 0
y = 0

# Count units of the sand if there is abyss under the last rock
while y < abyss:
    y, sand = pour(sand, abyss)
abyss_sand = sand

# Count units of the sand if there is floor under the last rock
floor = abyss + 2

while (500, 0) not in rock:
    _, sand = pour(sand, floor, False)
floor_sand = sand

# How many units of sand come to rest before sand starts flowing into the abyss below?
print("Part 1:", abyss_sand)

# How many units of sand come to rest?
print("Part 2:", floor_sand)
