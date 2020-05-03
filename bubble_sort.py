nums = [3, 2]

if nums[0] > nums[1]:
    nums.insert(0, nums.pop(1))
print(nums)

threes = [8, 10, 2]

for i in range(len(threes) - 1):
    swap = False
    for j in range(len(threes) - 1 - i):
        if threes[j] > threes[j+1]:
            threes[j], threes[j+1] = threes[j+1], threes[j]
            swap = True

    if swap == False:
        break

print(threes)
