from functools import reduce
from logging import info
from aocd.models import Puzzle
from aocd import submit
# from aocd import numbers
from aocd import lines
from copy import copy
puzzle = Puzzle(2021, 3)

# gamma = 0
# epsilon = 0

num_readings = len(lines)
num_bits = len(lines[0])
charsum = [0] * num_bits
for line in lines:
    for idx, c in enumerate(line):
        charsum[idx] += int(c)
gamma_str = ''
for c in charsum:
    gamma_str += '0' if c / num_readings < 0.5 else '1'

gamma = int(gamma_str,2)
epsilon = ~gamma & (2**num_bits-1)
# submit(gamma*epsilon, part="a")

possible_ox = copy(lines)
possible_c02 = copy(lines)
for idx, c in enumerate(gamma_str):
    if len(possible_ox) > 1:
        possible_ox = [r for r in possible_ox if r[idx] == c]
    if len(possible_c02) > 1:
        possible_c02 = [r for r in possible_c02 if r[idx] != c]
print(gamma_str)
print(possible_ox[0])
print(possible_c02[0])
ox = int(possible_ox[0], 2)
c02 = int(possible_c02[0], 2)
# submit(ox * c02, part="b")