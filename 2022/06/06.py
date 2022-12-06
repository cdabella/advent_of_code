from aocd import data, submit

from collections import deque

signal = data


def pt1():
    buffer_size = 4
    marker = deque(signal[:buffer_size], maxlen=buffer_size)
    for idx, data in enumerate(signal[buffer_size:], start=buffer_size):
        if len(set(marker)) == buffer_size:
            break
        marker.append(data)

    print(idx, marker)
    submit(idx)


def pt2():
    buffer_size = 14
    marker = deque(signal[:buffer_size], maxlen=buffer_size)
    for idx, data in enumerate(signal[buffer_size:], start=buffer_size):
        if len(set(marker)) == buffer_size:
            break
        marker.append(data)

    print(idx, marker)
    submit(idx)


if __name__ == "__main__":
    # pt1()
    pt2()
