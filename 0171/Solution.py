class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for ch in s:
            print(ch)
            num = num * 26 + (ord(ch) - ord('A') + 1)

        return num


s = 'ZY'
solution = Solution()
solution.titleToNumber(s)

