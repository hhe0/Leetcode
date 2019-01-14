class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if 0 == N:
            return 0
        elif 1 == N:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)


solution = Solution()
print(solution.fib(5))
