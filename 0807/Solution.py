class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowMax = [max(row) for row in grid]
        colMax = [max(col) for col in zip(*grid)]

        height = 0
        for k1, v1 in enumerate(grid):
            for k2, v2 in enumerate(v1):
                height += min(rowMax[k1], colMax[k2]) - v2

        return height


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
solution = Solution()
print(solution.maxIncreaseKeepingSkyline(grid))
