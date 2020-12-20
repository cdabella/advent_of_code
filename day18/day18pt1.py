
def evaluate(expr, pad=''):
    total = 0
    idx = 0

    current_num = None
    current_num_str = ''
    current_func = lambda x : x

    while idx < len(expr):
        c = expr[idx]

        # print(f"{pad}{idx}\t{total}\t{current_num_str}\t{current_num}\t{c}\t{expr[:idx+1]}")

        if c == '(':
            val, offset = evaluate(expr[idx+1:], pad + '  ')
            current_num = val
            idx += offset + 1
        elif c == ')':
            if current_num:
                total = current_func(current_num)
                current_num = None
            else:
                total = current_func(total)
            return total, idx
        elif c.isnumeric():
            current_num = int(c)
        elif c in '*+':
            if current_num:
                total = current_func(current_num)
                current_num = None
            else:
                total = current_func(total)

            if c == '*':
                current_func = lambda x: total * x
            elif c == '+':
                current_func = lambda x: total + x

        idx += 1

    if current_num:
        total = current_func(current_num)
    else:
        total = current_func(total)

    return total, idx

with open('input.txt') as f:
    total = 0
    while (line := f.readline()):
        line = line.strip().replace(' ', '')
        result, _ = evaluate(line)
        total += result
    print(total)
