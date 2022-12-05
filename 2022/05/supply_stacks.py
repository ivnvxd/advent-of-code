# https://adventofcode.com/2022/day/5

from copy import deepcopy


raw = []
stacks = [None]
moves = []

with open('input') as file:

    # iterate through first input part and stop at the first empty line
    for line in file:
        if line == '\n':
            break
        raw.append(line)

    # transpose raw data
    raw_transposed = list(zip(*raw))

    # keep only columns with useful data
    for i, stack in enumerate(raw_transposed):
        if i % 4 == 1:
            column = ''.join(stack[:-1]).lstrip()
            stacks.append(column)

    # make stacks deepcopy for the second part
    new_stacks = deepcopy(stacks)

    # read instructions
    for line in file:
        line = line.split()
        moves.append((int(line[1]), int(line[3]), int(line[5])))

# move all crates in reversed order
for amount, from_, to in moves:
    moved = stacks[from_][:amount][::-1]
    stacks[from_] = stacks[from_][amount:]
    stacks[to] = moved + stacks[to]

# collect top crates in one string
on_top = ''.join(item[0] for item in stacks[1:])

# After the rearrangement procedure completes, what crate ends up on top of each stack?
print('Part 1:', on_top)

# move all crates in given order
for amount, from_, to in moves:
    moved = new_stacks[from_][:amount]
    new_stacks[from_] = new_stacks[from_][amount:]
    new_stacks[to] = moved + new_stacks[to]

# collect top crates in one string
new_top = ''.join(item[0] for item in new_stacks[1:])

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
print('Part 2:', new_top)
