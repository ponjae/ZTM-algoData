class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for index in range(len(nums)):
            elem = nums[index]
            if seen.get(elem) is not None:
                return True
            else:
                seen[nums[index]] = True
        return False


class Solution2(object):
    def containsDuplicate(self, nums):
        dup = set(nums)
        if len(dup) == len(nums):
            return False
        else:
            return True
