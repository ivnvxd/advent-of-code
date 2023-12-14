# --- Day 7: No Space Left On Device ---
#
# https://adventofcode.com/2022/day/7

from collections import defaultdict

data = [line.strip() for line in open("input")]

path = ()
directories = defaultdict(int)
sizes_sum = 0

total_disk_space = 70000000
unused_space_needed = 30000000

for commands in data:
    line = commands.strip().split()

    if line[0] == "$":
        # ignore ls command
        if line[1] == "ls":
            continue

        # navigate between directories
        elif line[1] == "cd":
            if line[2] == "..":
                path = path[:-1]
            else:
                path += (line[2],)

    # ignore dir output
    elif line[0] == "dir":
        continue

    # add file size to the dict
    else:
        file_size = int(line[0])
        tmp = path

        # add file size to current directory and all parents directories
        for i in range(len(path)):
            directories[path] += file_size
            path = path[:-1]

        path = tmp

# determine needed to free size
enough = directories[("/",)]
unused_space = total_disk_space - enough
to_free = unused_space_needed - unused_space

# iterate through all directories and find the needed one
for current, size in directories.items():
    if size <= 100000:
        sizes_sum += size

    if size > to_free:
        enough = min(size, enough)

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
print("Part 1:", sizes_sum)

# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
print("Part 2:", enough)
