from aocd import data, lines, submit

# lines = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop""".split(
#     "\n"
# )


def pt1():
    cycle = 0
    X = 1
    idx = 0
    addx_cmd = False
    addx_value = 0
    signal_strengths = []
    while idx < len(lines):
        cycle += 1
        if (cycle - 20) % 40 == 0:

            signal_strengths.append(cycle * X)
        if addx_cmd:
            X += addx_value
            addx_value = 0
            addx_cmd = False
            idx += 1
        elif lines[idx] == "noop":
            idx += 1
        else:  # `addx #`
            addx_value = int(lines[idx].split(" ")[1])
            addx_cmd = True

    print(signal_strengths)
    print(sum(signal_strengths))
    # submit(sum(signal_strengths))


def pt2():
    cycle = 0
    X = 1
    idx = 0
    addx_cmd = False
    addx_value = 0
    CRT = ""
    while idx < len(lines):
        cycle += 1
        if X - 1 <= (cycle - 1) % 40 <= X + 1:
            CRT += "#"
        else:
            CRT += "."

        if addx_cmd:
            X += addx_value
            addx_value = 0
            addx_cmd = False
            idx += 1
        elif lines[idx] == "noop":
            idx += 1
        else:  # `addx #`
            addx_value = int(lines[idx].split(" ")[1])
            addx_cmd = True

    print("\n".join([CRT[i : i + 40] for i in range(0, len(CRT), 40)]))


if __name__ == "__main__":
    # pt1()
    pt2()
