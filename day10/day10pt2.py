from timeit import timeit

def main():
    with open ('input.txt') as f:
        data = [int(line.strip()) for line in f.readlines()]

    data.sort()

    paths = {0:1}
    for jolt in data:
        for i in [3, 2, 1]:
            previous_paths = paths.get(jolt - i, None)
            if previous_paths is not None:
                paths[jolt] = paths.get(jolt, 0) + previous_paths

    return paths[data[-1]]

# print(main())
print(timeit(main, number=10000))
