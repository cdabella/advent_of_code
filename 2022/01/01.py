from aocd import lines, submit

elves = []
elf = []
for line in lines:
    if line == "":
        elf = []
        elves.append(elf)
    else:
        elf.append(int(line))
# max sum of the nested list
# submit(max([sum(elf) for elf in elves]))

# sort and take the sum of three largest sums of the nested lists
# submit(sum(sorted([sum(elf) for elf in elves])[-3:]))
