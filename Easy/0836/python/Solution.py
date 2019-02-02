class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        a1, b1, c1, d1 = rec1
        a2, b2, c2, d2 = rec2

        return (a2 - c1) * (c2 - a1) < 0 and (b2 - d1) * (d2 - b1) < 0


rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]
solution = Solution()
print(solution.isRectangleOverlap(rec1, rec2))
