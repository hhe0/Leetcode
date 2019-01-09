import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return math.floor(x ** 0.5)


solution = Solution()
print(solution.mySqrt(8))

