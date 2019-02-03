class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_s = list(s)
        list_t = list(t)

        list_s.sort()
        list_t.sort()

        res = ''
        for i in range(0, len(list_t)):
            if i == len(list_t) - 1:
                res = list_t[i]
            elif list_t[i] != list_s[i]:
                res = list_t[i]
                break

        return res


s = ""
t = "a"
solution = Solution()
res = solution.findTheDifference(s, t)
print(res)
