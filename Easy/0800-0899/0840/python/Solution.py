class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid[0]) - 2):
                # print(i, j)
                temp = []
                for l in range(0, 3):
                    for m in range(0, 3):
                        # print(i+l, j+m)
                        temp.append(grid[i+l][j+m])

                if max(temp) != 9 or min(temp) != 1:
                    continue
                if len(set(temp)) != 9 and min(temp):
                    continue

                if grid[i][j] + grid[i][j+1] + grid[i][j+2] != 15:
                    continue
                if grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != 15:
                    continue
                if grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != 15:
                    continue
                if grid[i][j] + grid[i+1][j] + grid[i+2][j] != 15:
                    continue
                if grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != 15:
                    continue
                if grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != 15:
                    continue
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15:
                    continue
                if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15:
                    continue
                count += 1

        return count


# grid = [
#     [4, 3, 8, 4],
#     [9, 5, 1, 9],
#     [2, 7, 6, 2]
# ]
# grid = [
#     [3, 10, 2, 3, 4],
#     [4, 5, 6, 8, 1],
#     [8, 8, 1, 6, 8],
#     [1, 3, 5, 7, 1],
#     [9, 4, 9, 2, 9]
# ]
grid = [
    [4, 3, 8, 4],
    [9, 5, 1, 9],
    [2, 7, 6, 2]
]
solution = Solution()
res = solution.numMagicSquaresInside(grid)
print(res)
