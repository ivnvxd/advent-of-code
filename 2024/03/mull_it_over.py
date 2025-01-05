# --- Day 3: Mull It Over ---
#
# https://adventofcode.com/2024/day/3

from pathlib import Path
import re


def multiply(instruction):
    a, b = map(int, instruction.strip("mul()").split(","))
    return a * b


def part1(data):
    pattern = r"mul\(\d+,\d+\)"
    return sum(multiply(i) for i in re.findall(pattern, data))


def part2(data):
    pattern = r"mul\(\d+,\d+\)|(?:do|don't)\(\)"
    instructions = sorted([(m.start(), m.group()) for m in re.finditer(pattern, data)])

    total = 0
    enabled = True

    for _, instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            total += multiply(instruction)

    return total


if __name__ == "__main__":
    data = Path("input.txt").read_text()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
