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

def test_messages(f, rule_8, rule_11_42, rule_11_31):
    matches = 0
    while line:= f.readline().strip():
        for i in range(1,5):  # 5 determined through testing with given inputs
            rule = f'{rule_8}{rule_11_42}{{{i}}}{rule_11_31}{{{i}}}'
            if match := re.fullmatch(rule, line):
                matches += 1
                break
    return matches


def main():
    with open('input.txt', 'r') as f:
        rules_dict = parse_rules(f)
        # 0: [['8', '11']]

        # 8: [['42'], ['42', '8']]
        rule_8 = '^' + resolve_rule('42', rules_dict) + '+'

        # 11: [['42', '31'], ['42', '11', '31']]
        rule_11_42 = resolve_rule('42', rules_dict)
        rule_11_31 = resolve_rule('31', rules_dict)

        matches = test_messages(f, rule_8, rule_11_42, rule_11_31)

    return matches

if __name__ == '__main__':
    print(main())
