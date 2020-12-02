from itertools import combinations
from functools import reduce

target_sum = 2020
num_entries = 3

with open('input.txt') as f:
    report = [int(x) for x in f.readlines()]

pairs = combinations(report, num_entries)
print(f'Answer: {sum([reduce(lambda a, b: a*b, entries) for entries in pairs if sum(entries) == 2020])}')
