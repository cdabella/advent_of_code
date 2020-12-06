
with open ('input.txt') as f:
    all_group_answers = None
    any_group_answers = None

    all_group_count = []
    any_group_count = []
    while (line := f.readline()):
        if line == '\n':
            all_group_count.append(len(all_group_answers))
            any_group_count.append(len(any_group_answers))
            all_group_answers = None
            any_group_answers = None
        else:
            if all_group_answers is None:
                any_group_answers = all_group_answers = set(line.strip())
            else:
                all_group_answers = all_group_answers & set(line.strip())
                any_group_answers = any_group_answers.union(set(line.strip()))

    all_group_count.append(len(all_group_answers))
    any_group_count.append(len(any_group_answers))

    print(f'Anyone answered  : {sum(any_group_count)}')
    print(f'Everyone answered: {sum(all_group_count)}')
