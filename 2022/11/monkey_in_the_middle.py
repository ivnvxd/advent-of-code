# --- Day 11: Monkey in the Middle ---
#
# https://adventofcode.com/2022/day/11

from collections import deque
from copy import deepcopy
from math import lcm
from operator import add, mul
from re import findall


class Monkey:
    def __init__(self) -> None:
        self.items = None
        self.operation = None
        self.operation_value = None
        self.test = None
        self.if_true = None
        self.if_false = None
        self.inspections = 0

    def inspect(self) -> int:
        # remove the first item from monkey's items
        item = self.items.popleft()

        # if the old value is used two times in the operation
        if self.operation_value is None:
            return self.operation(item, item)
        else:
            return self.operation(item, self.operation_value)


def round(monkeys, div) -> None:
    for monkey in monkeys:
        monkey.inspections += len(monkey.items)

        while monkey.items:
            if div:
                item = monkey.inspect() % div
            else:
                item = monkey.inspect() // 3

            if item % monkey.test == 0:
                monkeys[monkey.if_true].items.append(item)
            else:
                monkeys[monkey.if_false].items.append(item)


def simulate(monkeys, rounds, div=None) -> int:
    for _ in range(rounds):
        round(monkeys, div)

    # find two monkeys with most inspections
    inspections = []

    for monkey in monkeys:
        inspections.append(monkey.inspections)
    first, second = sorted(inspections, reverse=True)[:2]

    return first * second


with open("input") as file:
    data = file.read().split("\n\n")

monkeys = []
divisors = []

# parse input and create list of Monkey objects
for m in data:
    lines = m.splitlines()

    operation_value = findall(r"\d+", lines[2])
    divisor = int(findall(r"\d+", lines[3])[0])

    monkey = Monkey()
    monkey.items = deque(map(int, findall(r"\d+", lines[1])))
    monkey.operation = add if "+" in lines[2] else mul
    monkey.operation_value = int(operation_value[0]) if operation_value else None
    monkey.test = divisor
    monkey.if_true = int(findall(r"\d+", lines[4])[0])
    monkey.if_false = int(findall(r"\d+", lines[5])[0])

    monkeys.append(monkey)
    divisors.append(divisor)

# make copy of all monkeys objects to use it in the second calculation
monkeys2 = deepcopy(monkeys)

answer1 = simulate(monkeys, 20)

# find the least common multiple of all divisors and use it to calculate 10k simulations
div = lcm(*divisors)
answer2 = simulate(monkeys2, 10000, div)

# What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
print("Part 1:", answer1)

# What is the level of monkey business after 10000 rounds?
print("Part 2:", answer2)
