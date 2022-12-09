# https://adventofcode.com/2022/day/9


class Rope:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'U':
            self.y += 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'L':
            self.x -= 1


data = [line.strip() for line in open('input')]

rope_length = 10
rope = []
path = []

# create variables for all knots
for n in range(rope_length):
    rope.append(Rope(0, 0))
    path.append({(0, 0)})

# read moves
for line in data:
    direction, moves = line.split()
    moves = int(moves)

    # move the rope
    for move in range(moves):

        # move the head
        rope[0].move(direction)

        # move the tail, iterate through all knots
        for i in range(1, len(rope)):

            # calculate horizontal and vertical offset
            horizontal = rope[i-1].x - rope[i].x
            vertical = rope[i-1].y - rope[i].y

            # if the head and the tail aren't touching and are in the same row or column
            if (abs(horizontal) > 1 and abs(vertical) == 0) or (abs(horizontal) == 0 and abs(vertical) > 1):
                rope[i].x += horizontal // 2
                rope[i].y += vertical // 2
                path[i].add((rope[i].x, rope[i].y))

            # if the head and the tail aren't touching and are NOT in the same row or column
            elif (abs(horizontal) > 1 and abs(vertical) > 0) or (abs(horizontal) > 0 and abs(vertical) > 1):
                rope[i].x += horizontal // abs(horizontal)
                rope[i].y += vertical // abs(vertical)
                path[i].add((rope[i].x, rope[i].y))

# Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
print('Part 1:', len(path[1]))

# Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
print('Part 2:', len(path[rope_length-1]))
