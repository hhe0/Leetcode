class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')

        res = ''
        for word in words:
            res += word[::-1]
            res += ' '
        res = res.rstrip()

        return res


s = "Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(s))

