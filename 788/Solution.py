class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        list = ['0', '1', '2', '5', '6', '8', '9']
        dict = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        res = []
        for num in range(0, N+1):
            flag = True
            for s in str(num):
                if s not in list:
                    flag = False
                    break
            if flag:
                res.append(str(num))
        # print(res)
        new_res = []
        for r in res:
            temp = ''
            for ch in r:
                temp += dict[ch]
            new_res.append(temp)

        # print(new_res)
        num = 0
        for i in range(0, len(res)):
            if res[i] != new_res[i]:
                num += 1

        return num


N = 10
solution = Solution()
res = solution.rotatedDigits(N)
print(res)
