# from aocd import submit
# from aocd import numbers
from aocd.models import Puzzle
from aocd import submit
from aocd import numbers

puzzle = Puzzle(2021, 1)
data = numbers
prev_depth = -1
increase_counter = 0
for depth in data:
    increase_counter += 1 if int(depth) > prev_depth else 0
    prev_depth = int(depth)

# submit(increase_counter - 1, part="a")

prev_depth = -1
increase_counter = 0
for idx in range(0, len(data)-3):
    depth = sum(data[idx:idx+3])
    increase_counter += 1 if depth > prev_depth else 0
    prev_depth = depth

# submit(increase_counter, part="b")
