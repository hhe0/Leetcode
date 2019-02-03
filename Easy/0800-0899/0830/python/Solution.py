class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        res = []

        for i in range(0, len(S)):
            # print(S[j], j, S[i], i)
            if S[i] != S[j]:
                if i - j >= 3:
                    res.append([j, i-1])
                j = i

        if i == len(S) - 1 and i - j >= 2:
            res.append([j, i])

        return res


S = 'abcdddeeeeaabbbcdd'
solution = Solution()
res = solution.largeGroupPositions(S)
print(res)