nums = [13, 5, 16, 2]


for i in range(1, len(nums)):
    for j in range(i - 1, -1, -1):
        if nums[j] > nums[i]:
            if j == 0:
                nums.insert(0, nums.pop(i))
                break
        else:
            nums.insert(j+1, nums.pop(i))
            break

print(nums)
