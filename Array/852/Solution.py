class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


A = [1, 3, 4, 1, 2]
solution = Solution()
solution.peakIndexInMountainArray(A)

