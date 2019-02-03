class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        for ch in s:
            if ch not in s_dict.keys():
                s_dict[ch] = 1
            else:
                s_dict[ch] += 1
        # print(s_dict)

        for key,value in s_dict.items():
            if value == 1:
                return s.index(key)

        return -1


s = 'l'
solution = Solution()
res = solution.firstUniqChar(s)
print(res)