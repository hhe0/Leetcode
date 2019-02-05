import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0, 1, 2]:
            return 0

        res = 1
        for num in range(2, n):
            is_prime = True
            for i in range(2, math.ceil(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                res += 1

        return res


n = 2
solution = Solution()
res = solution.countPrimes(n)
print(res)