class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        common = strs[0]

        for i in range(1, len(strs)):
            common = self.getCommonStr(common, strs[i])
            if not common:
                common = ''
                break

        return common

    def getCommonStr(self, str1, str2):
        l = min(len(str1), len(str2))
        i = 0
        while i < l:
            if str1[i] != str2[i]:
                break
            i += 1
        return str1[:i]


strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))


