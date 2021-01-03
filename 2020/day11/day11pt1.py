import pprint
from copy import deepcopy

def seat_check_generator(y,x,max_y, max_x):
    for y_diff in range(-1,2):
        for x_diff in range(-1,2):
            if y_diff == 0 and x_diff == 0:
                continue
            yield (y + y_diff,x + x_diff)

with open ('input.txt') as f:
    map = [list('.' + line.strip() + '.') for line in f.readlines()]

map = [['.'] * len(map[0])] + map + [['.'] * len(map[0])]

_FLOOR = '.'
_EMPTY = 'L'
_TAKEN = '#'

# (y,x)
max_y = len(map) - 1
max_x = len(map[0]) - 1

prev_map = deepcopy(map)
while True:
    for y, row in enumerate(map):
        for x, seat in enumerate(row):
            if seat == _FLOOR:
                continue
            elif seat == _EMPTY:
                map[y][x] = _TAKEN
                for (y_check, x_check) in seat_check_generator(y,x, max_y, max_x):
                    if prev_map[y_check][x_check] == _TAKEN:
                        map[y][x] = _EMPTY
                        break
            else:  # seat == _TAKEN
                adjacent = 0
                for (y_check, x_check) in seat_check_generator(y,x, max_y, max_x):
                    if prev_map[y_check][x_check] == _TAKEN:
                        adjacent += 1
                if adjacent >= 4:
                    map[y][x] = _EMPTY

    if prev_map == map:
        break
    prev_map = deepcopy(map)

print(len([seat for row in map for seat in row if seat == _TAKEN]))
