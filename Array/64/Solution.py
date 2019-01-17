class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        print(m, n)
        i = 0
        j = 0
        # while i < m and j < n:



grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
solution = Solution()
solution.minPathSum(grid)

