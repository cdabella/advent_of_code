from aocd import lines, submit

scoring = {
    "shape": {"rock": 1, "paper": 2, "scissors": 3},
    "result": {
        "lose": 0,
        "tie": 3,
        "win": 6,
    },
}

## Part 1
if False:
    guide_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    guide_values = list(guide_map)

    round_results = dict()
    for i in range(3):
        round_results[f"{guide_values[i]} {guide_values[(i+3)%3 +3]}"] = "tie"
        round_results[f"{guide_values[i]} {guide_values[(i+4)%3 +3]}"] = "win"
        round_results[f"{guide_values[i]} {guide_values[(i+5)%3 +3]}"] = "lose"

    total = 0
    for line in lines:
        result_score = scoring["result"][round_results[line]]
        shape_score = scoring["shape"][guide_map[line[-1]]]
        total += result_score + shape_score

    submit(total)

##Part 2
else:
    guide_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "tie",
        "Z": "win",
    }

    guide_values = list(guide_map)
    shapes = guide_values[:3]

    round_results = dict()
    for i in range(3):
        round_results[f"{shapes[i]} X"] = shapes[(i - 1) % 3]
        round_results[f"{shapes[i]} Y"] = shapes[i]
        round_results[f"{shapes[i]} Z"] = shapes[(i + 1) % 3]

    total = 0
    for line in lines:
        result_score = scoring["result"][guide_map[line[-1]]]
        shape_score = scoring["shape"][guide_map[round_results[line]]]
        total += result_score + shape_score
    submit(total)
