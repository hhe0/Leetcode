class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        else:
            return False


nums = [1, 2, 3, 1]
solution = Solution()
res = solution.containsDuplicate(nums)
print(res)
