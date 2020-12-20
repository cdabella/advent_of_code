import numpy as np

from dataclasses import dataclass
from typing import NamedTuple

@dataclass
class Tile:
    id: int = 0
    tile: np.ndarray = None
    north: int = None
    south: int = None
    east: int = None
    west: int = None
    isFixed: bool = False

def spaceprint(array):
    output = ''
    for row in array:
        outline = ''.join([str(int(col)) for col in row])
        # if monsters overlap, would need to replace >= 2
        outline = outline.replace('0', '.').replace('1', '#').replace('2', 'O')
        output += outline + '\n'
    print(output)

def is_valid_tile(tile: Tile):
    return sum([1 for dir in [tile.north, tile.south, tile.east, tile.west] if dir]) >=2

def is_corner(tile: Tile):
    return sum([1 for dir in [tile.north, tile.south, tile.east, tile.west] if dir]) == 2

def read_tile_file(file):
    with open(file, 'r') as f:
        raw_tiles = f.read().strip().split('\n\n')
    tiles = {}
    for raw_tile in raw_tiles:
        lines = raw_tile.split('\n')
        id = int(lines[0][5:-1])  # Tile 1123:
        # tile = np.array([list(line) for line in lines[1:]])
        tile = np.array(
            [[0 if c == '.' else 1 for c in line] for line in lines[1:]]
        )
        tiles[id] = Tile(id=id, tile=tile)
    return tiles

def align_all_tiles(tiles):
    tile_search = []
    while tiles:
        tile_search.append(tiles[list(tiles.keys())[0]])
        while (
            tile_search and
            (tile:= tile_search.pop()) and
            tile.id  in tiles
        ):
            tiles.pop(tile.id)
            tile.isFixed = True
            for id, next_tile in tiles.items():
                aligned = False
                if next_tile.isFixed:
                    aligned = align_fixed_tiles(tile, next_tile)
                else:
                    aligned = align_tiles(tile, next_tile)
                if aligned:
                    tile_search.append(next_tile)

def align_tiles(tile1, tile2):
    for _ in ['unflipped', 'flipped']:
        for _ in [0, 90, 180, 270]:
            aligned = align_fixed_tiles(tile1, tile2)
            if aligned:
                tile2.isFixed = True
                return True
            tile2.tile = np.rot90(tile2.tile)
        tile2.tile = np.fliplr(tile2.tile)
    return False

def align_fixed_tiles(tile1, tile2):
    aligned = False
    if np.all(np.equal(tile1.tile[0,  :], tile2.tile[-1, :])):
        tile1.north = tile2.id
        tile2.south = tile1.id
        aligned = True
    elif np.all(np.equal(tile1.tile[-1, :], tile2.tile[0,  :])):
        tile1.south = tile2.id
        tile2.north = tile1.id
        aligned = True
    elif np.all(np.equal(tile1.tile[:,  0], tile2.tile[:, -1])):
        tile1.west = tile2.id
        tile2.east = tile1.id
        aligned = True
    elif np.all(np.equal(tile1.tile[:, -1], tile2.tile[:,  0])):
        tile1.east = tile2.id
        tile2.west = tile1.id
        aligned = True
    return aligned

def generate_image(tiles, corners):
    num_tiles_dim = int(np.sqrt(len(tiles)))
    tile_shape = tiles[corners[0]].tile.shape[0] - 2  # Assume tiles are square
    image = np.zeros(
        (tile_shape * num_tiles_dim,
        tile_shape * num_tiles_dim)
    )
    image_tiles = np.zeros(
        (num_tiles_dim,
        num_tiles_dim)
    )
    current_row_id = [corner for corner in corners if (tiles[corner].south and tiles[corner].east)][0]
    next_row_id = tiles[current_row_id].south
    idx_y = 0
    while current_row_id:
        current_tile_id = current_row_id
        idx_x = 0
        while current_tile_id:
            image_tiles[idx_y // tile_shape, idx_x // tile_shape] = current_tile_id
            image[idx_y:idx_y+tile_shape, idx_x:idx_x+tile_shape] = (
                tiles[current_tile_id].tile[1:-1,1:-1]
            )
            current_tile_id = tiles[current_tile_id].east
            idx_x += tile_shape
        current_row_id = tiles[current_row_id].south
        idx_y += tile_shape
    return image

def load_sea_monster():
    monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]
    monster = np.array(
       [[0 if c == ' ' else 1 for c in line] for line in monster]
    )
    return monster

def count_monsters(image, monster):
    monster_sum = np.sum(monster)
    m_y, m_x = monster.shape
    monster_count = 0

    for flip in ['unflipped', 'flipped']:
        for rot in [0, 90, 180, 270]:
            i_y, i_x = image.shape
            out_image = np.copy(image)
            for y in range(0, i_y - m_y):
                for x in range(0, i_x - m_x):
                    if (
                        np.sum(
                            np.multiply(monster, image[y:y+m_y, x:x+m_x])
                        ) == monster_sum
                    ):
                        out_image[y:y+m_y, x:x+m_x] += monster
                        monster_count += 1
            if monster_count:
                # spaceprint(out_image)
                return monster_count

            image = np.rot90(image)
        image = np.fliplr(image)
    return monster_count


def part1(tiles):
    assert all([is_valid_tile(tile) for _, tile in tiles.items()])
    corners = [tile.id for _, tile in tiles.items() if is_corner(tile)]

    answer = 1
    for corner in corners:
        answer *= corner
    return corners, answer

def part2(tiles, corners):
    image = generate_image(tiles, corners)
    monster = load_sea_monster()
    m_count = count_monsters(image, monster)
    return np.sum(image) - m_count * np.sum(monster)

def main():
    tiles = read_tile_file('input.txt')
    align_all_tiles(tiles.copy())
    corners, p1_answer = part1(tiles)
    print(f'Part 1 answer: {p1_answer}\n')
    p2_answer = part2(tiles, corners)
    print(f'Part 2 answer: {p2_answer}')


if __name__ == '__main__':
    main()
