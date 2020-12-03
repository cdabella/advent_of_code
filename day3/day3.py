import numpy as np

slopes = np.asarray([
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
], dtype=int)

coords = np.zeros(slopes.shape, dtype=int)
num_trees = np.zeros(slopes.shape[0])

with open ('input.txt') as f:
    forest = [list(line[:-1]) for line in f.readlines()]  # could be more memory efficient here
    forest = np.asarray(forest)

for j, slope in enumerate(slopes):
    if forest[coords[j, 1], coords[j, 0]] == '#':
        num_trees[i] += 1
    coords[j] += slope
    coords[j, 0] = coords[j, 0] % forest.shape[1]

for i, row in enumerate(forest[1:,]):
    for j, slope in enumerate(slopes):
        # print(slope)
        if (i+1) % slope[1] == 0:
            if forest[coords[j, 1], coords[j, 0]] == '#':
                num_trees[j] += 1
            coords[j] += slope
            coords[j, 0] = coords[j, 0] % forest.shape[1]

print(num_trees)
