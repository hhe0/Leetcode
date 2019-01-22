class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        res_s = self.func(S)
        if res_s:
            res_s = ''.join(res_s)

        res_t = self.func(T)
        if res_t:
            res_t = ''.join(res_t)

        return res_s == res_t

    def func(self, S):
        stack = []
        for s in S:
            if s != '#':
                stack.append(s)
            elif stack:
                stack.pop()
        return stack


S = "a#c"
T = "b"
solution = Solution()
res = solution.backspaceCompare(S, T)
print(res)
