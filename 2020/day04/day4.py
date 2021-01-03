
_REQUIRED = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',

]

_OPTIONAL = [
    'cid',
]

_COUNT_ALL_FIELDS = len(_REQUIRED) + len(_OPTIONAL)
_COUNT_REQ_FIELDS = len(_REQUIRED)

valid = 0

with open ('input.txt') as f:
    passport = ''
    while (line := f.readline()):
        if line == '\n':
            entries = passport.split(' ')[:-1]
            if (len(entries) == _COUNT_ALL_FIELDS):
                valid += 1
            elif (len(entries) == _COUNT_REQ_FIELDS):
                if all([entry[:3] in _REQUIRED for entry in entries]):
                    valid += 1
            passport = ''
            continue
        else:
            passport += f'{line[:-1]} '

    # Final line
    entries = passport.split(' ')[:-1]
    if (len(entries) == _COUNT_ALL_FIELDS):
        valid += 1
    elif (len(entries) == _COUNT_REQ_FIELDS):
        if all([entry[:3] in _REQUIRED for entry in entries]):
            valid += 1

print(valid)
