class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        t_length = len(T)
        res = [0 for _ in range(t_length)]

        for key, value in enumerate(T):
            if stack:
                while stack and T[stack[-1]] < value:
                    res[stack[-1]] = key - stack[-1]
                    stack.pop()
            stack.append(key)

        return res


T = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
res = solution.dailyTemperatures(T)
print(res)