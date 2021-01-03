with open ('sample.txt') as f:
    data = [int(line.strip()) for line in f.readlines()]

diff_tracker = {1:0, 2:0, 3:0}

data.sort()  # O(nlogn)

data = [0] + data

for i, jolt in enumerate(data[1:]):  #O(n)
    diff_tracker[jolt - data[i]] += 1

diff_tracker[3] += 1

print(diff_tracker)
print(diff_tracker[1] * diff_tracker[3])
