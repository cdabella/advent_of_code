import re

def parse_rules(f):
    rules_dict = {}
    while ((line:= f.readline().strip()) and line != ''):
        rule = line.split(': ')
        if rule[1] in ['"a"', '"b"']:
            rules_dict[rule[0]] = rule[1][1]  # Grab a/b
        else:
            rules_dict[rule[0]] = [ group.split(' ') for group in rule[1].split(' | ')]
    return rules_dict

def resolve_rule(idx, rules):
    rule = rules[idx]
    if rule[0][0] in 'ab':
        return rule
    out_rule = '('
    for group in rule:
        out_rule += ''.join([resolve_rule(i, rules) for i in group]) + '|'
    return out_rule[:-1] + ')'

def test_messages(f, zero_rule):
    matches = 0
    while line:= f.readline().strip():
        if re.fullmatch(zero_rule, line):
            matches += 1
    return matches


def main():
    with open('input.txt', 'r') as f:
        rules_dict = parse_rules(f)
        zero_rule = resolve_rule('0', rules_dict)
        # breakpoint()
        print(zero_rule)
        matches = test_messages(f, zero_rule)
    return matches

if __name__ == '__main__':
    print(main())
