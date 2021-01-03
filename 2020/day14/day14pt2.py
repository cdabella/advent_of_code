with open ('input.txt') as f:
    mask = mask_AND = mask_OR = None
    memory = {}
    while (line := f.readline().strip()):
        line_split = line.split(' = ')
        if line_split[0][:4] == 'mask':
            mask = line_split[1]
            mask_AND = int(mask.replace('0','1').replace('X', '0'), 2)
            mask_OR = int(mask.replace('X', '0'), 2)
            mask = mask[::-1]
            continue
        else:
            addrs = [(int(line_split[0][4:-1]) | mask_OR) & mask_AND]
            for i, bit_mask in enumerate(mask):
                if bit_mask == 'X':
                    addrs = addrs + [pow(2,i) + addr for addr in addrs]
            for addr in addrs:
                memory[addr] = int(line_split[1])
    answer = 0
    for addr in memory:
        answer += memory[addr]
    print(answer)
