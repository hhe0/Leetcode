class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            n = n / 3

        return False if n != 1 else True


n = 45
solution = Solution()
res = solution.isPowerOfThree(n)
print(res)

