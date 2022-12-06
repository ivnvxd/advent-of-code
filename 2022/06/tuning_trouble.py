# https://github.com/mebeim/aoc/tree/master/2022#day-5---supply-stacks

with open('input') as file:
    data = file.read()

marker = None
marker_2 = None

for i in range(len(data) - 4):
    if len(set(data[i:i+4])) == 4:
        marker = i + 4
        break

for i in range(len(data) - 14):
    if len(set(data[i:i+14])) == 14:
        marker_2 = i + 14
        break

# How many characters need to be processed before the first start-of-packet marker is detected?
print('Part 1:', marker)

# How many characters need to be processed before the first start-of-message marker is detected?
print('Part 1:', marker_2)
