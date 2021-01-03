with open ('input.txt') as f:
    mask = mask_AND = mask_OR = None
    memory = {}
    while (line := f.readline().strip()):
        line_split = line.split(' = ')
        if line_split[0][:4] == 'mask':
            mask = line_split[1]
            mask_AND = int(mask.replace('X', '1'), 2)
            mask_OR = int(mask.replace('X', '0'), 2)
            continue
        else:
            memory_addr = int(line_split[0][4:-1])
            memory[memory_addr] = (int(line_split[1]) | mask_OR) & mask_AND

        answer = 0
        for addr in memory:
            answer += memory[addr]
    print(answer)
