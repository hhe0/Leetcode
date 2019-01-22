class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums[::2])


nums = [1, 4, 2, 3]
solution = Solution()
print(solution.arrayPairSum(nums))

