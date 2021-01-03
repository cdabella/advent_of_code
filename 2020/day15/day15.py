target_turn = 30000000

with open ('sample.txt') as f:
    initial_numbers = [int(x) for x in f.readline().strip().split(',')]

number_history = {}
turn_idx = 1

for num in initial_numbers:
    number_history[num] = turn_idx
    turn_idx += 1

num = 0
while turn_idx < target_turn:
    prev_turn = number_history.get(num, 0)
    number_history[num] = turn_idx
    num = turn_idx - prev_turn if prev_turn != 0 else 0
    turn_idx += 1

print(turn_idx, num)
