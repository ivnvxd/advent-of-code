# https://adventofcode.com/2022/day/1

calories = [line.strip() for line in open('input')]

sum_elves = []
one_elf = 0

for item in calories:
    if item == '':
        sum_elves.append(one_elf)
        one_elf = 0
    else:
        one_elf += int(item)

sum_elves.append(one_elf)

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
print(max(sum_elves))

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
print(sum(sorted(sum_elves, reverse=True)[0:3]))
