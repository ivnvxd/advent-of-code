# https://adventofcode.com/2023/day/4

from collections import defaultdict

with open("input.txt") as file:
    data = file.read().splitlines()

part1 = 0
cards = defaultdict(int)

for i in range(len(data)):
    card = data[i].split("|")

    left, right = card[0].split(":")[1], card[1]

    winning = list(map(int, left.split()))
    you_have = list(map(int, right.split()))

    win = len(set(winning) & set(you_have))

    card_points = 0
    if win > 0:
        card_points = 2 ** (win - 1)

    part1 += card_points

    cards[i] += 1
    for j in range(win):
        cards[i + 1 + j] += cards[i]

part2 = sum(cards.values())

# How many points are they worth in total?
print("Part 1:", part1)

# how many total scratchcards do you end up with?
print("Part 2:", part2)
