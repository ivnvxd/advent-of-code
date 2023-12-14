# --- Day 10: Cathode-Ray Tube ---
#
# https://adventofcode.com/2022/day/10

data = [line.strip() for line in open("input")]

cycle = 1
register = 1
signal = 0
crt = ""


def draw(cycle, register):
    if register <= cycle % 40 <= register + 2:
        return "#"
    else:
        return "."


for line in data:
    # draw current pixel
    crt += draw(cycle, register)
    cycle += 1

    if line.startswith("addx"):
        # add a new row when cycle % 40 gets > 0
        if cycle % 40 == 1:
            crt += "\n "

        # add cycle * register to total signal strength if cycle in [20, 60, 80, etc.]
        elif cycle % 40 == 20:
            signal += cycle * register

        crt += draw(cycle, register)
        cycle += 1

        # add value from addx command to register
        _, value = line.split()
        register += int(value)

    if cycle % 40 == 1:
        crt += "\n "
    elif cycle % 40 == 20:
        signal += cycle * register

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
print("Part 1:", signal)

# Render the image given by your program. What eight capital letters appear on your CRT?
print("Part 2:\n", crt)
