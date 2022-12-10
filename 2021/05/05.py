from aocd.models import Puzzle
from aocd import submit
# from aocd import numbers
from aocd import lines
from copy import copy

puzzle = Puzzle(2021, 5)

from collections import defaultdict

vent_map = defaultdict(int)

for line in lines:
    coords = line.split(' -> ')
    start, end = ([int(x) for x in coord.split(',')] for coord in coords)
    # Only horizontal and verticle
    if start[0] == end[0]:
        if start[1] > end[1]:
            for idx in range(end[1], start[1] + 1):
                vent_map[(start[0], idx)] += 1
        else:
            for idx in range(start[1], end[1] + 1):
                vent_map[(start[0], idx)] += 1
    elif start[1] == end[1]:
        if start[0] > end[0]:
            for idx in range(end[0], start[0] + 1):
                vent_map[(idx, start[1])] += 1
        else:
            for idx in range(start[0], end[0] + 1):
                vent_map[(idx, start[1])] += 1
    else:
        continue

counter = 0
for _,v in vent_map.items():
    counter += 1 if type(v) == int and v > 1 else 0

# submit(counter, part="a")

vent_map = defaultdict(int)

for line in lines:
    coords = line.split(' -> ')
    start, end = ([int(x) for x in coord.split(',')] for coord in coords)
    # Only horizontal and verticle
    if start[0] == end[0]:
        if start[1] > end[1]:
            for idx in range(end[1], start[1] + 1):
                vent_map[(start[0], idx)] += 1
        else:
            for idx in range(start[1], end[1] + 1):
                vent_map[(start[0], idx)] += 1
    elif start[1] == end[1]:
        if start[0] > end[0]:
            for idx in range(end[0], start[0] + 1):
                vent_map[(idx, start[1])] += 1
        else:
            for idx in range(start[0], end[0] + 1):
                vent_map[(idx, start[1])] += 1
    # diagonal
    # slope of 1
    elif (start[0] - end[0]) == (start[1] - end[1]):
        if start[1] > end[1]:
            for idx in range(start[1] - end[1] + 1):
                vent_map[(end[0] + idx, end[1] + idx)] += 1
        else:
            for idx in range(end[1] - start[1] + 1):
                vent_map[(start[0] + idx, start[1] + idx)] += 1
    # slope of -1
    elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
        if start[1] > end[1]:
            for idx in range(start[1] - end[1] + 1):
                vent_map[(end[0] + idx, end[1] - idx)] += 1
        else:
            for idx in range(end[1] - start[1] + 1):
                vent_map[(start[0] - idx, start[1] + idx)] += 1
    else:
        continue

counter = 0
for _,v in vent_map.items():
    counter += 1 if type(v) == int and v > 1 else 0
print(counter)
# submit(counter, part="b")