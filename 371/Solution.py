class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        else:
            return self.getSum(a ^ b, (a & b) << 1)


a = 1
b = 2
solution = Solution()
print(solution.getSum(a, b))