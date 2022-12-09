from aocd import data, lines, submit

from pprint import pprint as pp

# lines = """30373
# 25512
# 65332
# 33549
# 35390""".split(
#     "\n"
# )


def reset_heights():
    # chr(ord("0")-1)
    left_current_h = "/"
    right_current_h = "/"
    down_current_h = "/"
    up_current_h = "/"
    return left_current_h, right_current_h, down_current_h, up_current_h


def r_idx(idx):
    return -1 * idx - 1


def pt1():
    left_current_h, right_current_h, down_current_h, up_current_h = reset_heights()
    visible_trees = [["/" for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for idx_y in range(len(lines)):
        for idx_x in range(len(lines[0])):
            if lines[idx_y][idx_x] > left_current_h:
                left_current_h = lines[idx_y][idx_x]
                visible_trees[idx_y][idx_x] = left_current_h
            if lines[idx_y][r_idx(idx_x)] > right_current_h:
                right_current_h = lines[idx_y][r_idx(idx_x)]
                visible_trees[idx_y][r_idx(idx_x)] = right_current_h

        left_current_h, right_current_h, _, _ = reset_heights()
    for idx_x in range(len(lines[0])):
        for idx_y in range(len(lines)):
            if lines[idx_y][idx_x] > down_current_h:
                down_current_h = lines[idx_y][idx_x]
                visible_trees[idx_y][idx_x] = down_current_h
            if lines[r_idx(idx_y)][idx_x] > up_current_h:
                up_current_h = lines[r_idx(idx_y)][idx_x]
                visible_trees[r_idx(idx_y)][idx_x] = up_current_h
        _, _, down_current_h, up_current_h = reset_heights()
    pp(visible_trees)
    visible_tree_count = 0
    for row in visible_trees:
        for tree in row:
            visible_tree_count += 1 if tree != "/" else 0
    print(visible_tree_count)
    # submit(visible_tree_count)
    return visible_trees


def pt2():

    scenic_score = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    # ignore exterior trees
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[0]) - 1):
            if row == 3 and col == 2:
                print("")
            height = lines[row][col]
            if height == "/":
                continue
            left_view_distance = 1
            while col - left_view_distance >= 0:

                if lines[row][col - left_view_distance] >= height:
                    left_view_distance += 1
                    break
                left_view_distance += 1
            left_view_distance -= 1

            right_view_distance = 1
            while col + right_view_distance < len(lines[0]):
                if lines[row][col + right_view_distance] >= height:
                    right_view_distance += 1
                    break
                right_view_distance += 1
            right_view_distance -= 1

            up_view_distance = 1
            while row - up_view_distance >= 0:

                if lines[row - up_view_distance][col] >= height:
                    up_view_distance += 1
                    break
                up_view_distance += 1
            up_view_distance -= 1

            down_view_distance = 1
            while row + down_view_distance < len(lines):

                if lines[row + down_view_distance][col] >= height:
                    down_view_distance += 1
                    break
                down_view_distance += 1
            down_view_distance -= 1
            scenic_score[row][col] = (
                left_view_distance
                * right_view_distance
                * up_view_distance
                * down_view_distance
            )
    pp(scenic_score)
    best_scenic_score = max([max(row) for row in scenic_score])
    print(best_scenic_score)
    submit(best_scenic_score)


if __name__ == "__main__":
    visible_trees = pt1()
    pt2()
