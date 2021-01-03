
def read_file(file):
    with open(file, 'r') as f:
        public_keys = [int(x.strip()) for x in f.readlines()]
    return public_keys

def determine_loops(num, key):
    loop = 0
    transformed_num = 0
    while True:
        loop += 1
        if key == pow(num, loop, 20201227):
            break
        if loop % 100 == 0:
            print(f'Loop {loop}')
    return loop


def part1(public_keys):
    loops = [determine_loops(7, key) for key in public_keys]
    print(loops)
    private_key = pow(public_keys[0], loops[1], 20201227)
    print(f'P1 Answer: {private_key}')

def main():
    public_keys = read_file('input.txt')
    part1(public_keys)

if __name__ == '__main__':
    main()
