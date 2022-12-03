import sys
import functools

from aocd import lines, submit

## Pt 1
def pt1():
    total = 0
    for line in lines:
        ruck_size = len(line) // 2
        common_item = set(line[:ruck_size]).intersection(set(line[ruck_size:]))
        value = ord(common_item.pop())

        # ord values are A-Za-Z order, problem values are a-zA-Z
        if value < ord("a"):  # Capitol letter
            value = value - ord("A") + 27
        else:
            value = value - ord("a") + 1
        total += value
    submit(total)


def pt2():
    total = 0
    for i in range(0, len(lines), 3):
        rucks = [set(line) for line in lines[i : i + 3]]
        badge = functools.reduce(lambda x, y: x.intersection(y), rucks)
        value = ord(badge.pop())
        # ord values are A-Za-Z order, problem values are a-zA-Z
        if value < ord("a"):  # Capitol letter
            value = value - ord("A") + 27
        else:
            value = value - ord("a") + 1
        total += value
    submit(total)


if __name__ == "__main__":
    if False:
        pt1()
    else:
        pt2()
