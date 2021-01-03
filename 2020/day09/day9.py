preamble_length = 25
preamble = []

with open ('input.txt') as f:
    while len(preamble) < preamble_length:
        preamble.append(int(f.readline().strip()))

    idx = 0
    while (line := f.readline()):
        line = int(line.strip())
        valid = False
        for i, v1 in enumerate(preamble[idx: idx + preamble_length]):
            for v2 in preamble[idx + i: idx + preamble_length]:
                if line == v1 + v2:
                    valid = True
                    break
            if valid:
                break
        if not valid:
            print(f'Failed value: {line}')
            break

        idx += 1
        preamble.append(line)
    target = line
    idx = 0
    # print(preamble)
    for i, v in enumerate(preamble):
        target -= v
        # print('1', target, idx, preamble[idx:i + 1], v)
        while target < 0:
            target += preamble[idx]
            idx += 1
            # print('2', target, idx, preamble[idx:i + 1])
        # print('3', target, idx, preamble[idx:i + 1])
        if target == 0:
            # print('5',target, idx, preamble[idx:i + 1])
            print(f'Encryption weakness: ' +\
                  f'{min(preamble[idx:i + 1]) + max(preamble[idx:i + 1])}')
            break
    # print('5',target, idx)

        # print('4',target, idx, preamble[idx:i + 1])
