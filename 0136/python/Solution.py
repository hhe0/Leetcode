class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        for num in nums:
            pos = pos ^ num

        print(pos)
        return pos


solution = Solution()
solution.singleNumber([4, 1, 2, 1, 2])
