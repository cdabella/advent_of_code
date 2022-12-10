from aocd.models import Puzzle
from aocd import submit
# from aocd import numbers
from aocd import lines

puzzle = Puzzle(2021, 2)

x = 0
y = 0
for line in lines:
    linesplit = line.split(' ')
    if linesplit[0] == 'forward':
        x += int(linesplit[1])
    else:
        y += int(linesplit[1]) if linesplit[0] == 'down' else -1 * int(linesplit[1])
# submit(x*y, part="a")

x = 0
y = 0
aim = 0

for line in lines:
    linesplit = line.split(' ')
    if linesplit[0] == 'forward':
        x += int(linesplit[1])
        y += int(linesplit[1]) * aim
    else:
        aim += int(linesplit[1]) if linesplit[0] == 'down' else -1 * int(linesplit[1])
submit(x*y, part="b")