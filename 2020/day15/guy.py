##example inputs
input = [0,3,6] 
# input = [1,3,2]
# input = [2,1,3]

##puzzle input
# input = [0,6,1,7,2,19,20] 

nums = {n: i for i, n in enumerate(input[:-1])}
last = input[-1]

for i in range(len(input) - 1, 30000000 - 1):
    if last in nums:
        prev = nums[last]
        nums[last] = i
        last = i - prev
    else:
        nums[last] = i
        last = 0

print(last)
