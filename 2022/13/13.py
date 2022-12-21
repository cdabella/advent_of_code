from aocd import data, lines, submit

from typing import List, Tuple


def in_correct_order(left: List, right: List):
    # print(left, right)
    correct_order = None
    # if len(left) > len(right):
    #     return False
    for idx in range(len(left)):
        if idx >= len(right):
            return False
        if type(left[idx]) == int and type(right[idx]) == int:
            if left[idx] < right[idx]:
                return True
            if left[idx] > right[idx]:
                return False
        elif type(left[idx]) == int:
            correct_order = in_correct_order([left[idx]], right[idx])
        elif type(right[idx]) == int:
            correct_order = in_correct_order(left[idx], [right[idx]])
        else:
            correct_order = in_correct_order(left[idx], right[idx])

        if correct_order is not None:
            return correct_order
    return correct_order


# data = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""

# data = """[9]
# [[8,7,6]]"""

packet_pairs = data.split("\n\n")

# 257, 439, 3411
def pt1():
    packet_pairs = data.split("\n\n")
    corred_idxs = []
    for idx, packet_pair in enumerate(packet_pairs, start=1):
        left, right = tuple([eval(packet) for packet in packet_pair.split("\n")])
        ordered = in_correct_order(left, right)
        print(left, right, ordered)
        if ordered:
            corred_idxs.append(idx)
    print(corred_idxs)
    print(sum(corred_idxs))
    # submit(total)


def pt2():
    pass


if __name__ == "__main__":
    pt1()
    # pt2()
