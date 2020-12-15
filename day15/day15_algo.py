import seaborn as sns
import matplotlib.pyplot as plt

target_turn = 2020


# for initial_numbers in [[1,2,3],
#                         [1,3,2],
#                         [2,1,3],
#                         [2,3,1],
#                         [3,1,2],
#                         [3,2,1]]:
# for initial_numbers in [[1,2],
#                         [2,1]]:
for initial_numbers in [[1,2,3],]:
                        # [2,1]]:
    number_history = {}
    turn_idx = 1
    nums = []

    for num in initial_numbers:
        nums.append(num)
        number_history[num] = turn_idx
        turn_idx += 1

    num = 0
    while turn_idx < target_turn:
        nums.append(num)
        prev_turn = number_history.get(num, 0)
        number_history[num] = turn_idx
        num = turn_idx - prev_turn if prev_turn != 0 else 0
        turn_idx += 1

    print(initial_numbers, nums)
    sns.scatterplot(data=nums)
    plt.show()
    prev = None
    indices = []
    for idx, n in enumerate(nums):
        if prev == n:
            indices.append(idx)
        prev = n
    # print(indices)

    prev = 0
    indices = []
    for idx, n in enumerate(nums):
        if prev < n:
            indices.append(idx)
            prev = n
    # print(initial_numbers, indices)
    # sns.scatterplot(data=test_nums)
    # plt.show()

    # print(turn_idx, num)
