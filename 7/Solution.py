import sys


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        mystr = str(abs(x))
        if -2 ** 31 - 1 > int(mystr[::-1]) or int(mystr[::-1]) > 2 ** 31:
            return 0
        if x < 0:
            res = -1 * int(mystr[::-1])
        else:
            res = int(mystr[::-1])

        return res


solution = Solution()
print(solution.reverse(1534236469))
