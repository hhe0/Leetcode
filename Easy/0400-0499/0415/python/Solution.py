class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 有时间模拟一下加法的操作
        return str(int(num1) + int(num2))


num1 = '199'
num2 = '992'
solution = Solution()
res = solution.addStrings(num1, num2)
print(res)