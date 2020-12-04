import re
from collections import defaultdict

def hgt_parser(x):
    if x[-2:] == 'cm':
        return (150 <= int(x[:-2]) <= 193)
    elif x[-2:] == 'in':
        return (59 <= int(x[:-2]) <= 76)
    else:
        return False

_FIELDS = {
    'byr': lambda x: (re.fullmatch(r'\d{4}', x) and (1920 <= int(x) <= 2002)),
    'iyr': lambda x: (re.fullmatch(r'\d{4}', x) and (2010 <= int(x) <= 2020)),
    'eyr': lambda x: (re.fullmatch(r'\d{4}', x) and (2020 <= int(x) <= 2030)),
    'hgt': hgt_parser,
    'hcl': lambda x: re.fullmatch(r'#[\da-f]{6}', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.fullmatch(r'\d{9}', x),
    'cid': lambda x: True
}

_MAX_FIELD_COUNT = 8
_MIN_FIELD_COUNT = 7

valid = 0

with open ('input.txt') as f:
    passport = ''
    while (line := f.readline()):
        if line == '\n':
            entries = passport.split(' ')[:-1]
            passport = ''
            if (len(entries) < _MIN_FIELD_COUNT):
                continue
            elif (len(entries) == _MAX_FIELD_COUNT):
                if all([_FIELDS[entry[:3]](entry[4:]) for entry in entries]):
                    valid += 1
            elif (len(entries) == _MIN_FIELD_COUNT):
                all_fields_valid = True
                for entry in entries:
                    if entry[:3] == 'cid':
                        all_fields_valid = False
                        break
                    if not _FIELDS[entry[:3]](entry[4:]):
                        all_fields_valid = False
                        break
                if all_fields_valid:
                    valid += 1
        else:
            passport += f'{line[:-1]} '

#Final line
entries = passport.split(' ')[:-1]
if (len(entries) == _MAX_FIELD_COUNT):
    if all([_FIELDS[entry[:3]](entry[4:]) for entry in entries]):
        valid += 1
elif (len(entries) == _MIN_FIELD_COUNT):
    all_fields_valid = True
    for entry in entries:
        if entry[:3] == 'cid':
            all_fields_valid = False
            break
        if not _FIELDS[entry[:3]](entry[4:]):
            all_fields_valid = False
            break
    if all_fields_valid:
        valid += 1

print(valid)
