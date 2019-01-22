class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 0
        num = 0
        while i < len(digits):
            num = num * 10 + digits[i]
            i = i + 1
        numstr = str(num+1)
        numlist = []
        for numchar in numstr:
            numlist.append(int(numchar))

        return numlist


solution = Solution()
print(solution.plusOne([1, 2, 3]))

