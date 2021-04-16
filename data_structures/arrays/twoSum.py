# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        li = {}
        retLi = []
        for index in range(len(nums)):
            complement = target - nums[index]
            if li.get(complement) is not None:
                retLi.append(li.get(complement))
                retLi.append(index)
                return retLi
            else:
                li[nums[index]] = index


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
