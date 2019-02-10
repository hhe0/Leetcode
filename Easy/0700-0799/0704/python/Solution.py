class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i

        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
solution = Solution()
res = solution.search(nums, target)
print(res)
