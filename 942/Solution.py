class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        i = 0
        j = len(S)
        for ch in S:
            if ch == 'I':
                res.append(i)
                i += 1
            if ch == 'D':
                res.append(j)
                j -= 1
        res.append(i)

        return res


str = 'IDID'
solution = Solution()
print(solution.diStringMatch(str))
