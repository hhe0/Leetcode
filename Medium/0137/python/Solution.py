class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b


num = [1, 2, 2, 3, 3, 3, 2]
solution = Solution()
print(solution.singleNumber(num))
