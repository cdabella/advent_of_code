from aocd import lines, submit


def pt1():
    total = 0
    for line in lines:
        pairs = line.split(",")
        elf1_range = [int(x) for x in pairs[0].split("-")]
        elf1_assigns = set(range(elf1_range[0], elf1_range[1] + 1))
        elf2_range = [int(x) for x in pairs[1].split("-")]
        elf2_assigns = set(range(elf2_range[0], elf2_range[1] + 1))
        if elf1_assigns - elf2_assigns == set():
            total += 1
        elif elf2_assigns - elf1_assigns == set():
            total += 1
        else:
            continue
    submit(total)


def pt2():
    total = 0
    for line in lines:
        pairs = line.split(",")
        elf1_range = [int(x) for x in pairs[0].split("-")]
        elf1_assigns = set(range(elf1_range[0], elf1_range[1] + 1))
        elf2_range = [int(x) for x in pairs[1].split("-")]
        elf2_assigns = set(range(elf2_range[0], elf2_range[1] + 1))
        if len(elf1_assigns - elf2_assigns) != len(elf1_assigns):
            total += 1
    submit(total)


if __name__ == "__main__":
    # pt1()
    pt2()
