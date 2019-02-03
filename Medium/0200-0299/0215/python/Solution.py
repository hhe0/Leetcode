class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)

        return nums[k-1]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
solution = Solution()
print(solution.findKthLargest(nums, k))
