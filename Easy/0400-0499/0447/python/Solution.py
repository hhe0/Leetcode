class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(0, len(points) - 1):
            li = []
            for j in range(0, len(points)):
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                li.append(dis)
            print(li)
            sum += (len(li) - len(set(li)))

        return sum


points = [[0, 0], [1, 0], [2, 0]]
solution = Solution()
res = solution.numberOfBoomerangs(points)
print(res)