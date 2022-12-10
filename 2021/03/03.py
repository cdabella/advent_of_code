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
idx = 0
ox_bit = gamma_str[idx]
c02_bit = gamma_str[idx]
while idx < num_bits:
    if len(possible_ox) > 1:
        possible_ox = [r for r in possible_ox if r[idx] == ox_bit]
    if len(possible_c02) > 1:
        possible_c02 = [r for r in possible_c02 if r[idx] != c02_bit]
    idx += 1
    if idx == num_bits:
        break
    counter = 0
    for line in possible_ox:
        counter += int(line[idx])
    ox_bit = '0' if counter / len(possible_ox) < 0.5 else '1'
    counter = 0
    for line in possible_c02:
        counter += int(line[idx])
    c02_bit = '0' if counter / len(possible_c02) < 0.5 else '1'

ox = int(possible_ox[0], 2)
c02 = int(possible_c02[0], 2)
# submit(ox * c02, part="b")