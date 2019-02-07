class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B:
            return True
        if len(A) != len(B):
            return False

        list_A = list(A)
        list_B = list(B)
        for i in range(0, len(A)):
            temp = list_A[0]
            list_A.remove(list_A[0])
            list_A.append(temp)
            if list_A == list_B:
                return True

        return False


A = ''
B = ''
solution = Solution()
res = solution.rotateString(A, B)
print(res)