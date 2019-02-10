class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        for i in range(0, len(A[0])):
            flag = True
            for j in range(0, len(A) - 1):
                if A[j][i] > A[j+1][i]:
                    flag = False
                    break
            if not flag:
                res += 1

        return res


# A = ['cba', 'daf', 'ghi']
# A = ['a', 'b']
A = ["zyx", "wvu", "tsr"]
solution = Solution()
res = solution.minDeletionSize(A)
print(res)
