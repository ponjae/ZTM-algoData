class Solution(object):
    def moveZeroes(self, nums):
        newList = []
        for index in range(len(nums)-1, -1, -1):
            elem = nums[index]
            if elem == 0:
                newList = newList + [elem]
            else:
                newList = [elem] + newList
        nums[:] = newList


class Solution2:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        search = False
        while j < len(nums):
            if search:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    search = False
                    i += 1
                j += 1
            elif nums[i] == 0:
                search = True
            else:
                i += 1
                j += 1


sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)
