# https://adventofcode.com/2023/day/5

with open("input.txt") as file:
    data = file.read()

seeds_list, *maps = data.split("\n\n")

seeds = list(map(int, seeds_list.split(":")[1].split()))

seeds_pairs = []
for i in range(0, len(seeds), 2):
    seeds_pairs.append((seeds[i], seeds[i] + seeds[i + 1]))

for m in maps:
    ranges = []

    # Part 1
    lines = m.splitlines()[1:]
    for line in lines:
        ranges.append(list(map(int, line.split())))

    mapping = []
    for seed in seeds:
        for dst, src, rng in ranges:
            if src <= seed < src + rng:
                mapping.append(seed - src + dst)
                break
        else:
            mapping.append(seed)

    seeds = mapping

    # Part 2
    mapped_pairs = []
    while len(seeds_pairs) > 0:
        start, end = seeds_pairs.pop()

        for dst, src, rng in ranges:
            max_start = max(start, src)
            min_end = min(end, src + rng)

            if max_start < min_end:
                mapped_pairs.append((max_start - src + dst, min_end - src + dst))

                if max_start > start:
                    seeds_pairs.append((start, max_start))
                if min_end < end:
                    seeds_pairs.append((min_end, end))
                break
        else:
            mapped_pairs.append((start, end))

    seeds_pairs = mapped_pairs

part1 = min(seeds)
part2 = min(seeds_pairs)[0]

# What is the lowest location number that corresponds to any of the initial seed numbers?
print(part1)

# What is the lowest location number that corresponds to any of the initial seed numbers?
print(part2)
