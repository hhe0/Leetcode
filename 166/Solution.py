class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        a = numerator
        b = denominator
        res = ''

        res += str(a // b)

        d = a % b
        flag = False
        if not d:
            return res
        res += '.'
        while d:
            e = (d * 10) // b
            f = (d * 10) % b
            if f == d:
                flag = True
                break
            else:
                c = e
                d = f
            res += str(c)
        if flag:
            res += '('
            res += str(e)
            res += ')'
        return res


solution = Solution()
print(solution.fractionToDecimal(4, 333))
