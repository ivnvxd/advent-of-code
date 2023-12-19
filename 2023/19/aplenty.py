# --- Day 19: Aplenty ---
#
# https://adventofcode.com/2023/day/19


def get_workflows(workflows):
    work_map = {}

    for line in workflows.splitlines():
        name, rules = line[:-1].split("{")

        *first, last = rules.split(",")
        commands = []

        for rule in first:
            comparison, goto = rule.split(":")
            operator = ">" if ">" in comparison else "<"
            category, value = comparison.split(operator)
            commands.append((category, operator, int(value), goto))

        commands.append(last)
        work_map[name] = commands

    return work_map


def get_ratings(ratings):
    rating_list = []

    for line in ratings.splitlines():
        parts = line[1:-1].split(",")

        part_map = {}
        for part in parts:
            name, rating = part.split("=")
            part_map[name] = int(rating)

        rating_list.append(part_map)

    return rating_list


def process_part(work_map, part):
    workflow = "in"
    while workflow not in "RA":
        for command in work_map[workflow]:
            if isinstance(command, tuple):
                category, operator, value, goto = command
                if (operator == ">" and part[category] > value) or (
                    operator == "<" and part[category] < value
                ):
                    workflow = goto
                    break
            else:
                workflow = command
    return workflow


def sum_accepted_parts(rating_list, work_map):
    total = 0
    for part in rating_list:
        if process_part(work_map, part) == "A":
            total += sum(part.values())
    return total


def apply_rule(ranges, rule, work_map):
    category, operator, value, goto = rule
    lo, hi = ranges[category]

    if operator == ">":
        range_pass = (max(value + 1, lo), hi)
        range_fail = (lo, min(value, hi))
    else:
        range_pass = (lo, min(value - 1, hi))
        range_fail = (max(value, lo), hi)

    total = 0
    if range_pass[0] <= range_pass[1]:
        copy_pass = ranges.copy()
        copy_pass[category] = range_pass
        total += get_combinations(copy_pass, work_map, goto)

    if range_fail[0] <= range_fail[1]:
        ranges[category] = range_fail

    return total


def get_combinations(ranges, work_map, name="in"):
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    elif name == "R":
        return 0

    total = 0
    for rule in work_map[name]:
        if isinstance(rule, tuple):
            total += apply_rule(ranges, rule, work_map)
        else:
            total += get_combinations(ranges, work_map, rule)

    return total


def main():
    with open("input.txt") as file:
        data = file.read().strip()

    workflows, ratings = data.split("\n\n")
    work_map = get_workflows(workflows)
    rating_list = get_ratings(ratings)

    part1 = sum_accepted_parts(rating_list, work_map)

    ranges = {key: (1, 4000) for key in "xmas"}
    part2 = get_combinations(ranges, work_map)

    # Sort through all of the parts you've been given; what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?
    print("Part 1:", part1)

    # Consider only your list of workflows; the list of part ratings that the Elves wanted you to sort is no longer relevant. How many distinct combinations of ratings will be accepted by the Elves' workflows?
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
