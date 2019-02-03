class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        while i < len(A) and j < len(A):
            if A[i] % 2 == 0:
                i += 2
                continue
            if A[j] % 2 == 1:
                j += 2
                continue
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

        return A


arr = [4, 2, 5, 7]
solution = Solution()
print(solution.sortArrayByParityII(arr))

