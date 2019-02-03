class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = bin(n)[2:]
        print(a)
        for i in range(len(a) - 1):
            if a[i] == a[i+1]:
                return False
        return True


n = 101
solution = Solution()
res = solution.hasAlternatingBits(n)
print(res)
