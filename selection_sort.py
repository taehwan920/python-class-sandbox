import random

nums = [5, 2]

if nums[0] > nums[1]:
    nums[0], nums[1] = nums[1], nums[0]


nums = [10, 12, 4]

for i in range(len(nums) - 1):
    least_index = i
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            least_index = j
    nums[i], nums[least_index] = nums[least_index], nums[i]

print(nums)
