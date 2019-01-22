class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        while i < len(A):
            j = i + 1
            while j < len(A):
                if A[i] == A[j]:
                    return A[i]
                j += 1
            i += 1


solution = Solution()
print(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
