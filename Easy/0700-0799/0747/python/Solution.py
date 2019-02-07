import copy

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        temp = copy.copy(nums)
        nums.sort(reverse=True)
        if nums[0] >= nums[1] * 2:
            return temp.index(nums[0])
        else:
            return -1


nums = []
solution = Solution()
res = solution.dominantIndex(nums)
print(res)
