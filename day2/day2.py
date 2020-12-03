import re

#19-20 r: rfrrrhmrrrnrrtvrsrrr
format = r'(\d+)-(\d+) (.): (.+)'
count_part1_valid = 0
count_part2_valid = 0

with open('input.txt') as f:
    for line in f.readlines():
        low, high, character, password = re.match(format, line).groups()
        if int(low) <= password.count(character) <= int(high):
            count_part1_valid += 1

        length = len(password)

        # could optimize the number of checks against length
        if ((int(low) <= length and password[int(low) - 1] == character) !=
            (int(high) <= length and password[int(high) - 1] == character)):
            count_part2_valid += 1

print(f'Part 1 answer: {count_part1_valid}')
print(f'Part 2 answer: {count_part2_valid}')
