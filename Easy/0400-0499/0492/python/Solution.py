import math


class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w_start = math.ceil(math.sqrt(area))
        for i in range(w_start, area + 1):
            if area % i == 0:
                return [i, area // i]


area = 18
solution = Solution()
res = solution.constructRectangle(area)
print(res)
