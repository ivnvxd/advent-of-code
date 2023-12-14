# --- Day 2: Rock Paper Scissors ---
#
# https://adventofcode.com/2022/day/2

"""
opponent: A: Rock; B: Paper; C: Scissors
response: X: Rock; Y: Paper; Z: Scissors
"""

strategy = [line.strip() for line in open("input")]

points = 0
sec_points = 0

scores = {"X": 1, "Y": 2, "Z": 3}
outcome = {"lost": 0, "draw": 3, "won": 6}
variations = {
    ("A", "X"): "draw",
    ("A", "Y"): "won",
    ("A", "Z"): "lost",
    ("B", "X"): "lost",
    ("B", "Y"): "draw",
    ("B", "Z"): "won",
    ("C", "X"): "won",
    ("C", "Y"): "lost",
    ("C", "Z"): "draw",
}

sec_scores = {"X": 0, "Y": 3, "Z": 6}
sec_outcome = {"rock": 1, "paper": 2, "scissors": 3}
sec_variations = {
    ("A", "X"): "scissors",
    ("A", "Y"): "rock",
    ("A", "Z"): "paper",
    ("B", "X"): "rock",
    ("B", "Y"): "paper",
    ("B", "Z"): "scissors",
    ("C", "X"): "paper",
    ("C", "Y"): "scissors",
    ("C", "Z"): "rock",
}

for item in strategy:
    opponent, response = item.split()

    points += scores[response]
    points += outcome[variations[(opponent, response)]]

    sec_points += sec_scores[response]
    sec_points += sec_outcome[sec_variations[(opponent, response)]]

# What would your total score be if everything goes exactly according to your strategy guide?
print("Part 1:", points)

# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
print("Part 2:", sec_points)
