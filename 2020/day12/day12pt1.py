import numpy as np

direction = {
    0: 'N',
    1: 'E',
    2: 'S',
    3: 'W'
}

# Position (x,y) and direction (N, E, S, W)
_STATE = np.array([0, 0, 1])

# np.array([1, 0, 0],
#          [0, 1, 0],
#          [0, 0, 1])
_EYE = np.eye(3, dtype='int32')

_ACTIONS_TRANSITION = {
    'N' : lambda x: _EYE[0] * x,
    'E' : lambda x: _EYE[1] * x,
    'S' : lambda x: _EYE[0] * x * -1,
    'W' : lambda x: _EYE[1] * x * -1,
    'L' : lambda x: _EYE[2] * ((_STATE[2] - (x % 360) // 90) % 4 - _STATE[2]),
    'R' : lambda x: _EYE[2] * ((_STATE[2] + (x % 360) // 90) % 4 - _STATE[2]),
    'F' : lambda x: _ACTIONS_TRANSITION[direction[_STATE[2]]](x)
}

with open ('input.txt') as f:
    while (line := f.readline()):
        line = line.strip()
        _STATE += _ACTIONS_TRANSITION[line[0]](int(line[1:]))

print(np.abs(_STATE[0]) + np.abs(_STATE[1]))
