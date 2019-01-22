class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None
        res = [s[0]]
        for i in s:
            if i not in res:
                res.append(i)
            else:
                break

s = 'abcabcbb'
solution = Solution()
solution.lengthOfLongestSubstring(s)
