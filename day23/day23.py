#!/usr/bin/env python3

def read_file(file):
    with open(file, 'r') as f:
        cups = [int(x) for x in f.read().strip()]
    return cups

def read_file_as_ll(file):
    with open(file, 'r') as f:
        cups = [int(x) for x in f.read().strip()]
    ll = {
        'first': cups[0],
        'last': cups[-1]
    }

    for idx, cup in enumerate(cups[1:-1]):
        ll[cup] = {
            'next' : cups[idx + 2],
            'prev' : cups[idx]
        }

    ll[ll['first']] = {
        'next': cups[1],
        'prev': cups[-1]
    }

    ll[ll['last']] = {
        'next' : ll['first'],
        'prev' :  cups[-2]
    }
    return ll

def extends_ll_to_n(ll, n=1000000):
    num_cups = len(ll) - 2
    ll[ll['first']]['prev'] = n
    ll[ll['last']]['next'] = num_cups + 1
    for new_cup in range(num_cups+1, n+1):
        ll[new_cup] = {
            'next' : new_cup + 1,
            'prev' : new_cup - 1
        }
    ll[n]['next'] = ll['first']
    ll['last'] = n

def index_cups_to_one(cups):
    idx = cups.index(1)
    return cups[idx+1:] + cups[:idx]

def shuffle_cups(cups, iters, debug=False):
    if debug:
        # print(iters)
        print(cups[:20], cups[-20:])
    cup_pickup = 3
    max_cup_label = len(cups)
    if iters == 0:
        return cups
    current_cup = cups[0]
    pick_up = cups[1:4]
    destination = current_cup - 1 if current_cup - 1 != 0 else max_cup_label
    while destination not in cups[4:]:
        destination = destination - 1 if destination - 1 != 0 else max_cup_label
    idx = cups[4:].index(destination)
    cups = cups[4:][:idx+1] + pick_up + cups[4:][idx+1:] + [current_cup]
    return shuffle_cups(cups, iters - 1, debug)

def unroll_ll(cups, start_cup):
    out_cups = [start_cup]
    current_cup = cups[start_cup]['next']
    while current_cup != start_cup:
        # print(out_cups)
        out_cups.append(current_cup)
        current_cup = cups[current_cup]['next']
    return out_cups

def shuffle_ll_cups(cups, iterations):
    cup_pickup = 3
    max_cup = len(cups) - 2
    current_cup = cups['first']
    for i in range(iterations):
        lifted_cups = []
        next_cup = cups[current_cup]['next']
        for _ in range(cup_pickup):
            lifted_cups.append(next_cup)
            next_cup = cups[next_cup]['next']

        target_cup = current_cup -1
        target_cup = target_cup if target_cup > 0 else max_cup
        while target_cup in lifted_cups:
            target_cup -= 1
            target_cup = target_cup if target_cup > 0 else max_cup

        # current cup
        cups[current_cup]['next'] = next_cup
        cups[next_cup]['prev'] = current_cup

        # lifted cups
        cups[lifted_cups[0]]['prev'] = target_cup
        cups[lifted_cups[-1]]['next'] = cups[target_cup]['next']

        # target + 1
        cups[cups[target_cup]['next']]['prev'] = lifted_cups[-1]
        cups[target_cup]['next'] = lifted_cups[0]

        current_cup = next_cup
    return cups


def part1():
    cups = read_file('input.txt')
    shuffled_cups = shuffle_cups(cups, 100)
    print(shuffled_cups)
    answer = [str(x) for x in index_cups_to_one(shuffled_cups)]
    answer = ''.join(answer)
    print(f'P1 Answer: {answer}')

def part1_ll():
    cups = read_file_as_ll('input.txt')
    shuffled_cups = shuffle_ll_cups(cups, 100)
    unrolled_cups = unroll_ll(shuffled_cups, 1)
    answer = [str(x) for x in unrolled_cups[1:]]
    answer = ''.join(answer)
    print(f'P1 Answer: {answer}')

def part2():
    cups = read_file_as_ll('input.txt')
    extends_ll_to_n(cups, 1000000)
    shuffled_cups = shuffle_ll_cups(cups, 10000000)
    next_cup = shuffled_cups[1]['next']
    next_next_cup = shuffled_cups[next_cup]['next']
    print(f'P2 Answer: {next_cup * next_next_cup}')

def main():
    # part1()
    part1_ll()
    part2()

if __name__ == '__main__':
    main()
