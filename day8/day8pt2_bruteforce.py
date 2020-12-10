# This problem could be solved with DFS and tracking nop/jmp with a stack
with open ('input.txt') as f:
    lines = f.readlines()

    attempted_fix_idx = set()
    finish_dx = len(lines)

    while True:
        tried_fix = False
        acc = 0
        idx = 0
        visited_idx = set()

        while True:
            visited_idx.add(idx)
            line = lines[idx].strip().split(' ')
            if line[0] == 'nop':
                if idx not in attempted_fix_idx and not tried_fix:
                    attempted_fix_idx.add(idx)
                    tried_fix = True
                    idx += int(line[1])
                else:
                    idx += 1
            elif line[0] == 'acc':
                acc += int(line[1])
                idx += 1
            elif line[0] == 'jmp':
                if idx not in attempted_fix_idx and not tried_fix:
                    attempted_fix_idx.add(idx)
                    tried_fix = True
                    idx += 1
                else:
                    idx += int(line[1])
            if idx in visited_idx:
                break
            elif idx == finish_dx:
                break

        if idx == finish_dx:
            break

    print(acc)
