class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dict = {}
        for key, point in enumerate(points):
            dict[key] = point[0] * point[0] + point[1] * point[1]

        dict = sorted(dict.items(), key=lambda x: x[1])

        res = []
        i = 0
        while i < K:
            res.append(points[dict[i][0]])
            i += 1

        return res


points = [[3, 3], [5, -1], [-2, 4]]
solution = Solution()
solution.kClosest(points, 2)

