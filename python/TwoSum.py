"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1]."""

# My Solution
def twoSumMySolution(nums,target) :
    size = len(nums)
    i = 0 #3
    j = 1
    for i in range(size):
        for j in range(1,size):
            # print(i,j)
            res = nums[i] + nums[j]
            if res == target:
                return [i,j]

nums = [2, 7, 11, 15]
target = 18
Res = twoSumMySolution(nums,target)
print(Res)

# Optimized Solution
def twoSumOptimizedSolution(nums, target):
    mapping = {}

    for index, val in enumerate(nums):
        diff = target - val
        if diff in mapping:
            return [index, mapping[diff]]
        else:
            mapping[val] = index



Res = twoSumOptimizedSolution(nums,target)
print(Res)
