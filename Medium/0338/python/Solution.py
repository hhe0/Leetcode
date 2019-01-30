class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []

        for n in range(0, num+1):
            bnum = bin(n)[2:]
            temp = 0

            for b in bnum:
                if b == '1':
                    temp += 1
            res.append(temp)

        return res


num = 5
solution = Solution()
res = solution.countBits(num)
print(res)
