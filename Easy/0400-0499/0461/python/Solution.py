class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = x ^ y
        count = 0
        while res > 0:
            if res & 1 == 1:
                count += 1

            res = res >> 1

        return count


x = 2
y = 13
solution = Solution()
print(solution.hammingDistance(x, y))
