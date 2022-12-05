from aocd import lines, submit


def init():
    # Drawing
    #     [D]
    # [N] [C]
    # [Z] [M] [P]
    #  1   2   3

    _crate_size = 4

    draw_end = lines.index("")
    drawing = lines[: draw_end - 1]  # skip index
    inputs = lines[draw_end + 1 :]

    # include empty 1st index to make later indexing easier
    stacks = [[] for _ in range(len(drawing[0]) // _crate_size + 2)]

    # Reverse for proper stack ordering (FILO)
    for line in reversed(drawing):
        for idx in range(0, len(line), _crate_size):
            crate = line[idx + 1]
            if crate == " ":
                continue
            stacks[(idx // _crate_size) + 1].append(crate)
    return stacks, inputs


def pt1():
    stacks, inputs = init()
    for input in inputs:
        # "move 3 from 8 to 9"
        _, num_crates, _, from_stack, _, to_stack = tuple(input.split(" "))
        for i in range(int(num_crates)):
            stacks[int(to_stack)].append(stacks[int(from_stack)].pop())
    output = ""
    for stack in stacks[1:]:
        output += stack[-1]
    print(output)
    # submit(output)


def pt2():
    stacks, inputs = init()
    for input in inputs:
        # "move 3 from 8 to 9"
        _, num_crates, _, from_stack, _, to_stack = tuple(input.split(" "))
        stacks[int(to_stack)].extend(stacks[int(from_stack)][-1 * int(num_crates) :])
        stacks[int(from_stack)] = stacks[int(from_stack)][: -1 * int(num_crates)]
    output = ""
    for stack in stacks[1:]:
        output += stack[-1]
    print(output)
    # submit(output)


if __name__ == "__main__":
    # pt1()
    pt2()
