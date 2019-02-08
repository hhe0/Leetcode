class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False
        if len(A) == 1:
            return True

        increment = False
        flag = False
        for i in range(1, len(A)):
            if not flag and A[i] != A[i - 1]:
                flag = True
                if A[i] > A[i - 1]:
                    increment = True
                else:
                    increment = False

            if flag:
                if increment:
                    if A[i] < A[i - 1]:
                        return False
                else:
                    if A[i] > A[i - 1]:
                        return False

        return True


A = [1, 1, 1]
solution = Solution()
res = solution.isMonotonic(A)
print(res)