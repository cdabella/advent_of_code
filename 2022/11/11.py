from aocd import data, lines, submit

from collections import deque


class Monkey:
    def __init__(
        self, name="", items=deque(), op=lambda x: x, test=None, worry_loss=True
    ):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.items_inspected = 0
        self.worry_loss = worry_loss

    def round(self):
        for _ in range(len(self.items)):
            self.items_inspected += 1
            item = self.items.popleft()
            item = self.op(item)
            if self.worry_loss:
                item = item // 3
            self.test(item)

    def catch(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"Monkey {self.name} inspected items {self.items_inspected} times."


def test_wrapper(divisor, true_monkey: Monkey, false_monkey: Monkey, scaling):
    def test(item):
        # item = item % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
        item = item % scaling
        # if item == 0:
        if item % divisor == 0:
            true_monkey.catch(item)
        else:
            false_monkey.catch(item)

    return test


def parse_monkies(data, worry_loss=True):
    monkies = []
    raw_monkies = data.split("\n\n")
    divisors = []
    # init monkies
    for idx, raw_monkey in enumerate(raw_monkies):
        lines = raw_monkey.split("\n")
        items = deque([int(x) for x in lines[1].split(": ")[1].split(", ")])
        op = eval(f"lambda old: {lines[2].split(' = ')[1]}")
        divisors.append(int(lines[3].split(" ")[-1]))
        monkies.append(Monkey(str(idx), items, op, worry_loss))
    scaling = 1
    print(divisors)
    for d in divisors:
        scaling *= d
    # Add monkey tests
    for idx, raw_monkey in enumerate(raw_monkies):
        lines = raw_monkey.split("\n")
        divisor = int(lines[3].split(" ")[-1])
        true_monkey = monkies[int(lines[4].split(" ")[-1])]
        false_monkey = monkies[int(lines[5].split(" ")[-1])]
        monkies[idx].test = test_wrapper(divisor, true_monkey, false_monkey, scaling)
    return monkies


data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def pt1():
    rounds = 20
    monkies = parse_monkies(data)
    for round in range(rounds):
        if round % 1000 == 1:
            for m in monkies:
                print(m)
                print(m.items)
        for monkey in monkies:
            print(monkey.items)
            monkey.round()
    sorted_monkies = sorted(monkies, key=lambda x: x.items_inspected, reverse=True)

    monkey_business = (
        sorted_monkies[0].items_inspected * sorted_monkies[1].items_inspected
    )
    print(sorted_monkies)
    print(monkey_business)
    # submit(monkey_business)


def pt2():
    rounds = 1
    monkies = parse_monkies(data, worry_loss=False)
    for round in range(rounds):
        # if round == 0 or round % 1000 == 1:
        #     # print(f"Round {round}")
        #     # print("\n".join([str(m) for m in monkies]))
        #     for m in monkies:
        #         print(m)
        #         print(m.items)
        for monkey in monkies:
            print(monkey)
            print(monkey.items)
            monkey.round()
    sorted_monkies = sorted(monkies, key=lambda x: x.items_inspected, reverse=True)

    monkey_business = (
        sorted_monkies[0].items_inspected * sorted_monkies[1].items_inspected
    )
    print(sorted_monkies)
    print(monkey_business)


if __name__ == "__main__":
    # pt1()
    pt2()
