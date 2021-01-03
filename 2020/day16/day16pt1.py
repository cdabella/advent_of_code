import re

field_re = r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)'

with open('input.txt') as f:
    valid = set()

    # Parse field rules
    line = f.readline().strip()
    while line != '':
        results = re.match(field_re, line).groups()
        for i in range(int(results[1]), int(results[2]) + 1):
            valid.add(i)
        for i in range(int(results[3]), int(results[4]) + 1):
            valid.add(i)
        line = f.readline().strip()

    # Parse your ticket
    line = f.readline().strip()
    while line != '':
        line = f.readline().strip()

    invalid = 0
    # Parse nearby tickets
    line = f.readline()  # Ignore header
    line = f.readline().strip()
    while line != '':
        for i in [int(field) for field in line.split(',')]:
            if i not in valid:
                invalid += i
        line = f.readline().strip()
    print(invalid)
