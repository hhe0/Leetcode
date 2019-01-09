class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numstr = str(x)
        if x < 0:
            return False
        else:
            print(str(int(numstr[::-1])), numstr)
            if str(int(numstr[::-1])) == numstr:
                return True
            return False


solution = Solution()
print(solution.isPalindrome(10))

