# https://adventofcode.com/2022/day/8

with open('input', 'r') as file:
    data = file.read().splitlines()

# get dimensions of the grid
height = len(data)
width = len(data[0])

# count trees on the edge
visible_trees = height * 2 + width * 2 - 4

best_score = 0

for i, row in enumerate(data):
    # skip the first and last lines
    if i == 0 or i == height - 1:
        continue

    for j, tree in enumerate(row):
        # skip the first and last columns
        if j == 0 or j == width - 1:
            continue

        visible = [True, True, True, True]

        # find the first tree in the north that is higher tan the current one
        for north in range(i - 1, -1, -1):
            if data[north][j] >= tree:
                visible[0] = False
                break

        # find the first tree in the east that is higher tan the current one
        for east in range(j + 1, width):
            if row[east] >= tree:
                visible[1] = False
                break

        # find the first tree in the south that is higher tan the current one
        for south in range(i + 1, height):
            if data[south][j] >= tree:
                visible[2] = False
                break

        # find the first tree in the west that is higher tan the current one
        for west in range(j - 1, -1, -1):
            if row[west] >= tree:
                visible[3] = False
                break

        # check if no trees in any direction weren't higher than the current one
        if any(visible):
            visible_trees += 1

        # count how many trees can be seen from the current one
        score = (i - north) * (east - j) * (south - i) * (j - west)
        best_score = max(score, best_score)

# Consider your map; how many trees are visible from outside the grid?
print('Part 1:', visible_trees)

# Consider each tree on your map. What is the highest scenic score possible for any tree?
print('Part 2:', best_score)
