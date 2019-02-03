class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        max = 1
        for i in range(0, len(s) - 1):
            temp = [s[i]]
            length = 1
            for j in range(i+1, len(s)):
                if s[j] not in temp:
                    temp.append(s[j])
                    length += 1
                else:
                    break
            if length > max:
                max = length

        return max


s = 'pwwkew'
solution = Solution()
res = solution.lengthOfLongestSubstring(s)
print(res)