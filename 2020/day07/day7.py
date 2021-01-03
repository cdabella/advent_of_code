from collections import deque, defaultdict

my_bag = 'shiny gold'

# light red bags contain 1 bright white bag, 2 muted yellow bags.

with open ('sample_inf.txt') as f:
    # inner -> outer :  num_bags
    contained_directed_graph = defaultdict(lambda: {})

    # outer -> inner :  num_bags
    containing_directed_graph = defaultdict(lambda: {})

    while (line := f.readline()):
        line = line.strip()
        split_line = line.split(' bags contain ')
        outer_bag_type = split_line[0]

        inner_bags = split_line[1].split(', ')
        for inner_bag in inner_bags:
            details = inner_bag.split(' ')
            if details[0] == 'no':
                break
            num_container = int(details[0])
            inner_bag_type = f'{details[1]} {details[2]}'
            contained_directed_graph[inner_bag_type][outer_bag_type] = num_container
            containing_directed_graph[outer_bag_type][inner_bag_type] = num_container

    queue = deque([my_bag])
    answer_bags_pt1 = set()

    while queue:
        current_bag = queue.popleft()
        for bag in contained_directed_graph[current_bag]:
            if bag in answer_bags_pt1:
                continue
            answer_bags_pt1.add(bag)
            queue.append(bag)

    # Wrapper function protects against infinite loops
    # Memoization improves runtime performance by avoiding recalculating solved bags
    def bag_unpacker_wrapper():
        visited = {}

        def bag_unpacker(current_bag):
            contained = visited.get(current_bag, None)
            if contained:
                return contained
            else:
                visited[current_bag] = float('inf')
            sum = 1
            for bag in containing_directed_graph[current_bag]:
                sum += containing_directed_graph[current_bag][bag] * bag_unpacker(bag)
            visited[current_bag] = sum
            return sum

        return bag_unpacker

    num_bags = bag_unpacker_wrapper()(my_bag) - 1  # Remove my_bag from the count

    print(f'Number of bags that can contain my {my_bag}: {len(answer_bags_pt1)}')
    print(f'Number of bags my {my_bag} contains: {num_bags}')
