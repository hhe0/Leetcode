class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        for i in range(len(A[0])):
            res.append([])

        for j in range(len(A[0])):
            for k in range(len(A)):
                res[j].append(A[k][j])

        return res


solution = Solution()
solution.transpose([[1, 2, 3], [4, 5, 6]])
