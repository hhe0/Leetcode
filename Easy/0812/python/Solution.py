class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        for i in range(0, len(points) - 2):
            for j in range(i+1, len(points) - 1):
                for k in range(j+1, len(points)):
                    # print(i, j, k, max_area)
                    x1 = points[i][0]
                    y1 = points[i][1]
                    x2 = points[j][0]
                    y2 = points[j][1]
                    x3 = points[k][0]
                    y3 = points[k][1]

                    res = (1 / 2) * abs((x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2))
                    max_area = res if res > max_area else max_area

        return max_area


points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
solution = Solution()
res = solution.largestTriangleArea(points)
print(res)