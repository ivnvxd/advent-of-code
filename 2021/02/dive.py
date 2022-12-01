# https://adventofcode.com/2021/day/2

moves = [line.strip() for line in open('input')]

horizontal = 0
depth = 0
aim = 0

for item in moves:
    direction, amount = item.split(' ')

    if direction == 'forward':
        horizontal += int(amount)
        depth += aim * int(amount)
    elif direction == 'down':
        aim += int(amount)
    elif direction == 'up':
        aim -= int(amount)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
print(horizontal * aim) # 1690020

# Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
print(horizontal * depth)
