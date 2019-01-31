class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for a in A:
            res.append(a ** 2)
        res.sort()

        return res


A = [-7, -3, 2, 3, 11]
solution = Solution()
solution.sortedSquares(A)
