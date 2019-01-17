class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        return (num - 1) % 9 + 1


num = 10
solution = Solution()
print(solution.addDigits(num))
