import numpy as np

# Position (x,y)
_STATE_SHIP = np.array([0, 0])
_STATE_WAYPOINT = np.array([10, 1])

_RIGHT = np.array([[0, -1],
                  [1,  0]])

_LEFT = np.array([[ 0, 1],
                   [-1, 0]])

# np.array([1, 0,
#          [0, 1])
_EYE = np.eye(2, dtype='int32')

with open ('input.txt') as f:
    while (line := f.readline()):
        line = line.strip()
        if line[0] == 'N':
            _STATE_WAYPOINT += _EYE[1] * int(line[1:])
        elif line[0] == 'S':
            _STATE_WAYPOINT += _EYE[1] * int(line[1:]) * -1
        elif line[0] == 'E':
            _STATE_WAYPOINT += _EYE[0] * int(line[1:])
        elif line[0] == 'W':
            _STATE_WAYPOINT += _EYE[0] * int(line[1:]) * -1
        elif line[0] == 'L':
            _STATE_WAYPOINT = np.dot(
                                        _STATE_WAYPOINT,
                                        np.linalg.matrix_power(
                                            _LEFT,
                                            (int(line[1:]) % 360) // 90)
                                    )
        elif line[0] == 'R':
            _STATE_WAYPOINT = np.dot(
                                        _STATE_WAYPOINT,
                                        np.linalg.matrix_power(
                                            _RIGHT,
                                            (int(line[1:]) % 360) // 90)
                                    )
        elif line[0] == 'F':
            _STATE_SHIP += _STATE_WAYPOINT * int(line[1:])

print(np.abs(_STATE_SHIP[0]) + np.abs(_STATE_SHIP[1]))
