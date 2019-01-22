from string import ascii_uppercase
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lst = []
        dct = dict(enumerate(ascii_uppercase, start=1))

        while n:
            mod = n % 26
            n //= 26
            if mod == 0:
                mod = 26
                n -= 1
            lst.append(mod)

        return ''.join([dct[i] for i in reversed(lst)])


n = 26

solution = Solution()
solution.convertToTitle(n)

