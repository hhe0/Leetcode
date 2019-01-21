class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return 0
        A.sort()
        for i in range(len(A)-1, -1, -1):
            if i >= 2 and A[i-2] + A[i-1] > A[i]:
                return A[i-2] + A[i-1] + A[i]

        return 0


A = [3,6,2,3]
solution = Solution()
res = solution.largestPerimeter(A)
print(res)