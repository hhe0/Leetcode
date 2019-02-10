class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]

        return nums[0]


nums = [1, 2]
# nums = [3, 4, 5, 1, 2]
solution = Solution()
res = solution.findMin(nums)
print(res)
