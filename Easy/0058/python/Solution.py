class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        start = False
        res = ''
        while i >= 0:
            if s[i] != ' ':
                start = True
                res += s[i]
            elif start:
                break
            i -= 1

        return len(res)


s = 'a 1 '
solution = Solution()
res = solution.lengthOfLastWord(s)
print(res)
