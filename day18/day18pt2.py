stack = []

functions = {
    '+' : lambda x,y: x+y,
    '*' : lambda x,y: x*y
}

def evaluate(expr, pad=''):
    num_stack = [0]
    func_stack = ['+']
    idx = 0
    while idx < len(expr):
        # print(f"{pad}{idx}\t{num_stack}\t{func_stack}\t\t{expr[:idx+1]}")
        c = expr[idx]

        if c == ' ':
            idx +=1
            continue
        elif c.isnumeric():
            num_stack.append(int(c))
        elif c == '*':
            while func_stack:
                num_stack.append(
                    functions[func_stack.pop()](
                        num_stack.pop(),
                        num_stack.pop()
                    )
                )
            func_stack.append(c)
        elif c == '+':
            func_stack.append(c)
        elif c == '(':
            val, offset = evaluate(expr[idx+1:], pad='  ')
            idx += offset
            num_stack.append(val)
        elif c == ')':
            while func_stack:
                num_stack.append(
                    functions[func_stack.pop()](
                        num_stack.pop(),
                        num_stack.pop()
                    )
                )
            return num_stack.pop(), idx+1

        idx += 1

    while func_stack:
        num_stack.append(
            functions[func_stack.pop()](
                num_stack.pop(),
                num_stack.pop()
            )
        )
    return num_stack.pop(), idx

with open('input.txt') as f:
    total = 0
    while (line := f.readline()):
        # print('#' * 80)
        line = line.strip()
        result, _ = evaluate(line)
        # print(result)
        total += result
    print(total)
