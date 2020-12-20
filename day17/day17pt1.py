import numpy as np

def spaceprint(array):
    z = array.shape[0]
    for i in range(z):
        output = ''
        for row in array[i]:
            output += ''.join(['#' if col else '.' for col in row]) + '\n'
        print(f'z={i}')
        print(output)

rounds = 6

with open('input.txt') as f:
    starting_plane = [[c=='#' for c in line.strip()] for line in f.readlines()]

# pocket diminsion, not pandas
pd = np.zeros(
    (
        3+rounds*2,
        2+len(starting_plane)+rounds*2,
        2+len(starting_plane[0])+rounds*2
    ),
    dtype='int32'
)

pd[rounds+1, 1+rounds:-1*rounds-1, 1+rounds:-1*rounds-1] = starting_plane

for round in range(rounds):
    next_pd = np.copy(pd)
    for z in range(1, pd.shape[0]-1):
        for y in range(1, pd.shape[1]-1):
            for x in range(1, pd.shape[2]-1):
                num_neighbors = np.sum(pd[z-1:z+2,y-1:y+2,x-1:x+2]) - pd[z,y,x]
                if pd[z,y,x] == 1:
                    if num_neighbors == 2 or num_neighbors == 3:
                        next_pd[z,y,x] = 1
                    else:
                        next_pd[z,y,x] = 0
                elif pd[z,y,x] == 0 and num_neighbors == 3:
                    next_pd[z,y,x] = 1
    pd = next_pd
print(np.sum(pd))
