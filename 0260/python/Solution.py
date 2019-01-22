class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        n = len(bin(res)) - 3

        a, b = 0, 0
        for num in nums:
            if num >> n & 1:
                a ^= num
            else:
                b ^= num
        return [b, a]


nums = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4]
solution = Solution()
print(solution.singleNumber(nums))

