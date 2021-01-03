from copy import deepcopy
import timeit

def main():
    def seat_check_generator(y_diff,x_diff, y_start,x_start,max_y, max_x):
        y = y_start + y_diff
        x = x_start + x_diff
        while 0 <= y <= max_y and 0 <= x <= max_x:
            yield y, x
            y += y_diff
            x += x_diff

    with open ('input.txt') as f:
        map = [list(line.strip()) for line in f.readlines()]

    _FLOOR = '.'
    _EMPTY = 'L'
    _TAKEN = '#'

    slopes = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

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
                    for y_diff,x_diff in slopes:
                        for (y_check, x_check) in seat_check_generator(y_diff,x_diff, y,x, max_y, max_x):
                            if prev_map[y_check][x_check] == _TAKEN:
                                map[y][x] = _EMPTY
                                break
                            elif prev_map[y_check][x_check] == _EMPTY:
                                break
                        if map[y][x] == _EMPTY:
                            break
                else:  # seat == _TAKEN
                    adjacent = 0
                    for y_diff,x_diff in slopes:
                        for (y_check, x_check) in seat_check_generator(y_diff,x_diff, y,x, max_y, max_x):
                            if prev_map[y_check][x_check] == _TAKEN:
                                adjacent += 1
                                break
                            elif prev_map[y_check][x_check] == _EMPTY:
                                break
                    if adjacent >= 5:
                        map[y][x] = _EMPTY

        if prev_map == map:
            break
        prev_map = deepcopy(map)

    print(len([seat for row in map for seat in row if seat == _TAKEN]))

main()
# print(timeit.timeit(main, number=1))
