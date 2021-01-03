with open ('sample.txt') as f:
    acc = 0
    idx = 0
    lines = f.readlines()
    visited_idx = set()
    while True:
        prev_idx = idx
        visited_idx.add(idx)
        line = lines[idx].strip().split(' ')
        if line[0] == 'nop':
            idx += 1
        elif line[0] == 'acc':
            acc += int(line[1])
            idx += 1
        elif line[0] == 'jmp':
            idx += int(line[1])

        if idx in visited_idx:
            idx = prev_idx
            break
    print(acc)
    # while (line := f.readline()):
