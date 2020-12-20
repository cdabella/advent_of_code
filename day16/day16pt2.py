import re

field_re = r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)'

with open('input.txt') as f:
    valid = set()
    fields = set()
    rules = {}
    # Parse field rules
    line = f.readline().strip()
    while line != '':
        results = re.match(field_re, line).groups()

        fields.add(results[0])
        rules[results[0]] = set()

        for i in range(int(results[1]), int(results[2]) + 1):
            rules[results[0]].add(i)
        for i in range(int(results[3]), int(results[4]) + 1):
            rules[results[0]].add(i)

        valid = valid.union(rules[results[0]])

        line = f.readline().strip()

    invalid_fields = [set() for _ in fields]

    # Parse your ticket
    f.readline()
    line = f.readline().strip()
    my_ticket = [int(field) for field in line.split(',')]
    for i, val in enumerate(my_ticket):
        for rule in rules:
            if val not in rules[rule]:
                invalid_fields[i].add(rule)
    f.readline()

    # Parse nearby tickets
    f.readline()  # Ignore header
    line = f.readline().strip()
    while line != '':
        ticket_fields = [i in valid for i in [int(field) for field in line.split(',')]]
        if not all(ticket_fields):
            line = f.readline().strip()
            continue
        for i, val in enumerate([int(field) for field in line.split(',')]):
            for rule in rules:
                if val not in rules[rule]:
                    invalid_fields[i].add(rule)

        line = f.readline().strip()

    answer = 1

    valid_fields = [fields.difference(field) for field in invalid_fields]
    final_fields = {}
    while len(fields) > 0:
        for i, possible_fields in enumerate(valid_fields):
            if len(possible_fields) == 0:
                continue
            elif len(possible_fields) == 1:
                final_field = possible_fields.pop()
                fields.remove(final_field)
                if 'departure' in final_field:
                    answer *= my_ticket[i]
            else:
                valid_fields[i] = possible_fields & fields

    print(answer)
