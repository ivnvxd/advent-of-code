# https://adventofcode.com/2023/day/7


def score(hand):
    counts = [hand.count(card) for card in hand]

    strength = 0
    if 5 in counts:
        strength = 6
    elif 4 in counts:
        strength = 5
    elif 3 in counts:
        if 2 in counts:
            strength = 4
        else:
            strength = 3
    elif 2 in counts:
        if counts.count(2) == 4:
            strength = 2
        else:
            strength = 1

    return strength


def joker(hand):
    variants = [hand]
    available = "23456789TQKA"

    for card in hand:
        if card == "J":
            for a in available:
                variants.append(hand.replace(card, a))

    return variants


with open("input.txt") as file:
    data = file.read().strip()

card_strengths = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}
new_card_strengths = card_strengths.copy()
new_card_strengths["J"] = 1

hands = []

for line in data.split("\n"):
    hand, bid = line.split()
    hands.append([hand, int(bid)])

for hand in hands:
    cards = hand[0]

    strength = score(cards)
    strength2 = max(map(score, joker(cards)))

    weights = [strength, [int(card_strengths.get(card, card)) for card in cards]]
    weights2 = [strength2, [int(new_card_strengths.get(card, card)) for card in cards]]

    hand += [weights] + [weights2]

# Part 1
hands.sort(key=lambda x: x[2])

part1 = 0
for i, hand in enumerate(hands, 1):
    part1 += i * hand[1]

# Part 2
hands.sort(key=lambda x: x[3])

part2 = 0
for i, hand in enumerate(hands, 1):
    part2 += i * hand[1]

# What are the total winnings?
print("Part 1:", part1)

# What are the new total winnings?
print("Part 2:", part2)
