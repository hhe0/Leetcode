class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if max(A) - min(A) <= 2 * K:
            return 0
        else:
            return max(A) - min(A) - 2 * K


A = [1, 3, 6]
K = 3
solution = Solution()
print(solution.smallestRangeI(A, K))
