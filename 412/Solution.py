class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        res = []
        while i <= n:
            temp = ''
            if i % 3 == 0:
                temp += 'Fizz'
            if i % 5 == 0:
                temp += 'Buzz'
            if temp == '':
                temp = str(i)
            res.append(temp)
            i += 1

        return res


n = 1
solution = Solution()
print(solution.fizzBuzz(n))

