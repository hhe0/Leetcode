class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index_list = []
        for i in range(0, len(S)):
            if S[i] == C:
                index_list.append(i)

        res = []
        for j in range(0, len(S)):
            dist = len(S)
            for k in range(0, len(index_list)):
                distance = abs(index_list[k] - j)
                if distance < dist:
                    dist = distance
            res.append(dist)

        return res


S = 'loveleetcode'
C = 'e'
solution = Solution()
res = solution.shortestToChar(S, C)
print(res)
