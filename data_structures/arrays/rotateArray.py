class Solution(object):
    def rotate(self, nums, k):
        factor = k % len(nums)
        nums[:] = nums[-factor:] + nums[:-factor]


class Solution2:
    def rotate(self, nums, k):
        nums[:] = nums[len(nums)-k:len(nums)] + nums[:len(nums)-k]


solver = Solution()
nums = [1, 2]
solver.rotate(nums, 3)
print(nums)
