class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        set = []
        for i in range(n):
            set.append(i)

        res = []
        for val in set:
            print(val)

n = 4
k = 2
solution = Solution()
solution.combine(n, k)

