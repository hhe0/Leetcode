class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        max = 0

        for num in nums:
            if num == 1:
                stack.append(num)
            else:
                tmp = len(stack)
                max = tmp if tmp > max else max
                stack = []
        if stack and len(stack) > max:
            max = len(stack)

        return max


nums = [1]
solution = Solution()
solution.findMaxConsecutiveOnes(nums)
