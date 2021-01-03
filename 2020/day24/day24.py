import numpy as np
from tqdm import tqdm
from copy import copy, deepcopy
from pprint import pprint

class Tile:
    def __init__(self, coords, color=0):
        self.coords : np.array =  coords
        self.color = color
    def __repr__(self):
        return f'{self.coords} {self.color}'

def read_file(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

hex_coords = {
    'nw': np.array([-1,  0,  1], dtype='int32'),
    'ne': np.array([ 0,  1,  1], dtype='int32'),
    'e':  np.array([ 1,  1,  0], dtype='int32'),
    'se': np.array([ 1,  0, -1], dtype='int32'),
    'sw': np.array([ 0, -1, -1], dtype='int32'),
    'w':  np.array([-1, -1,  0], dtype='int32'),
}

def parse_direction(direction):
    global hex_coords
    coord = np.zeros((3,), dtype='int32')
    current_step = ''
    for c in direction:
        current_step += c
        if current_step in hex_coords:
            coord += hex_coords[current_step]
            current_step = ''
        else:
            continue
    return coord

# def count_black(tiles):
#     num_black = 0
#     for _, val in tiles.items():
#         num_black += val
#     return num_black

def count_black(tiles):
    num_black = 0
    for _, tile in tiles.items():
        num_black += tile.color
    return num_black

# def part1(directions):
#     tiles = {}
#     for direction in directions:
#         coord = tuple(parse_direction(direction))
#         tiles[coord] = tiles.get(coord, 0) ^ 1
#     num_black = count_black(tiles)
#     print(f'P1 Answer: {num_black}')
#     return tiles

def part1(directions):
    tiles = {}
    for direction in directions:
        coord = parse_direction(direction)
        coord_key = tuple(coord)
        tile = tiles.get(coord_key, Tile(coord))
        tile.color ^= 1
        tiles[coord_key] = tile
    num_black = count_black(tiles)
    print(f'P1 Answer: {num_black}')
    return tiles

def another_day(tiles):
    global hex_coords
    next_tiles = copy(tiles)
    x_coords = [t[0] for t in tiles]
    y_coords = [t[1] for t in tiles]
    z_coords = [t[2] for t in tiles]
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    z_min, z_max = min(z_coords), max(z_coords)
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                tile = np.array([x,y,z])
                num_black_neighbors = 0
                for _, neighbor_coords in hex_coords.items():
                    num_black_neighbors += tiles.get(
                        tuple(tile + neighbor_coords),
                        0
                    )

                if tiles.get(tuple(tile), 0) == 0 and num_black_neighbors == 2:
                    next_tiles[tuple(tile)] = 1
                elif tiles.get(tuple(tile), 0) == 1 and (
                    2 < num_black_neighbors or num_black_neighbors == 0
                ):
                    next_tiles[tuple(tile)] = 0
    return next_tiles

def extend_tiles(tiles):
    next_tiles = copy(tiles)
    for _, tile in tiles.items():
        for _, direction in hex_coords.items():
            neighbor_coords = tile.coords + direction
            neighbor_key = tuple(neighbor_coords)
            if neighbor_key not in next_tiles:
                next_tiles[neighbor_key] = Tile(neighbor_coords)
    return next_tiles

def update_tiles(tiles):
    next_tiles = deepcopy(tiles)
    for tilekey, tile in tiles.items():
        num_black_neighbors = 0
        for _, direction in hex_coords.items():
            neighbor_key = tuple(tile.coords + direction)
            if neighbor_key in tiles:
                num_black_neighbors += tiles[neighbor_key].color

        if tile.color == 0 and num_black_neighbors == 2:
            next_tiles[tilekey].color = 1
        elif tile.color == 1 and (
            2 < num_black_neighbors or num_black_neighbors == 0
        ):
            next_tiles[tilekey].color = 0
    return next_tiles

def another_dollar(tiles):
    global hex_coords
    tiles = extend_tiles(tiles)
    tiles = update_tiles(tiles)
    return tiles

def part2(tiles):
    for day in tqdm(range(100)):
        # tiles = another_day(tiles)
        tiles = another_dollar(tiles)
    print(f'P2 Answer: {count_black(tiles)}')


def main():
    directions = read_file('input.txt')
    tiles = part1(directions)
    part2(tiles)

if __name__ == '__main__':
    main()
