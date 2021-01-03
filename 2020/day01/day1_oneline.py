from itertools import combinations
from functools import reduce

target_sum = 2020
num_entries = 3

with open('input.txt') as f: print(f'Answer: {sum([reduce(lambda a, b: a*b, entries) for entries in combinations([int(x) for x in f.readlines()], num_entries) if sum(entries) == 2020])}')
