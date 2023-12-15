# --- Day 15: Lens Library ---
#
# https://adventofcode.com/2023/day/15


def hash(data):
    value = 0
    for char in data:
        value += ord(char)
        value *= 17
        value %= 256

    return value


def main():
    with open("input.txt") as input:
        data = input.read().strip().split(",")

    part1 = 0
    boxes = [{} for _ in range(256)]
    for step in data:
        part1 += hash(step)

        if step.endswith("-"):
            label = step[:-1]
            boxes[hash(label)].pop(label, None)
        else:
            label, focal = step.split("=")
            boxes[hash(label)][label] = int(focal)

    part2 = sum(
        i * j * focal
        for i, box in enumerate(boxes, start=1)
        for j, focal in enumerate(box.values(), start=1)
    )

    # Run the HASH algorithm on each step in the initialization sequence. What is the sum of the results?
    print("Part 1:", part1)

    # With the help of an over-enthusiastic reindeer in a hard hat, follow the initialization sequence. What is the focusing power of the resulting lens configuration?
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
