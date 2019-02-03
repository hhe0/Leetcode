class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            if self.isDividingNumber(i):
                res.append(i)

        return res

    def isDividingNumber(self, number):
        for n in str(number):
            if int(n) == 0 or number % int(n) != 0:
                return False

        return True


left = 1
right = 22
solution = Solution()
print(solution.selfDividingNumbers(left, right))

