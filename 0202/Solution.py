class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        n_str = str(n)
        while n_str != '1':
            # print(record, n_str)
            if n_str in record:
                return False
            res = 0
            record.append(n_str)
            for s in n_str:
                res += int(s) ** 2
            n_str = str(res)

        return True


n = 2
solution = Solution()
res = solution.isHappy(n)
print(res)
