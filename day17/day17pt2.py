import numpy as np

rounds = 6

with open('input.txt') as f:
    starting_plane = [[c=='#' for c in line.strip()] for line in f.readlines()]

# pocket diminsion, not pandas
pd = np.zeros(
    (
        3+rounds*2,
        3+rounds*2,
        2+len(starting_plane)+rounds*2,
        2+len(starting_plane[0])+rounds*2
    ),
    dtype='int32'
)

pd[rounds+1,rounds+1, 1+rounds:-1*rounds-1, 1+rounds:-1*rounds-1] = starting_plane

for round in range(rounds):
    next_pd = np.copy(pd)
    for w in range(1, pd.shape[0]-1):
        for z in range(1, pd.shape[1]-1):
            for y in range(1, pd.shape[2]-1):
                for x in range(1, pd.shape[3]-1):
                    num_neighbors = np.sum(pd[w-1:w+2,z-1:z+2,y-1:y+2,x-1:x+2]) - pd[w,z,y,x]
                    if pd[w,z,y,x] == 1:
                        if num_neighbors == 2 or num_neighbors == 3:
                            next_pd[w,z,y,x] = 1
                        else:
                            next_pd[w,z,y,x] = 0
                    elif pd[w,z,y,x] == 0 and num_neighbors == 3:
                        next_pd[w,z,y,x] = 1
    pd = next_pd
print(np.sum(pd))
