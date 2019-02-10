class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, bound):
            if x ** i > bound:
                break
            for j in range(0, bound):
                if y ** j > bound:
                    break
                num = x ** i + y ** j
                if num > bound:
                    break
                else:
                    if num not in res:
                        res.append(num)

        res.sort()

        return res


x = 3
y = 5
bound = 15
solution = Solution()
res = solution.powerfulIntegers(x, y, bound)
print(res)
