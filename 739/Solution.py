class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(T)):
            flag = False
            num = 1
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    flag = True
                    res.append(num)
                    break
                num += 1
            if not flag:
                res.append(0)

        return res


T = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
solution.dailyTemperatures(T)
