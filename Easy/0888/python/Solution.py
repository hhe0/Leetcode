class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(A), sum(B)
        setB = set(B)

        for i in range(len(A)):
            if A[i] + (sumB - sumA) // 2 in setB:
                return [A[i], A[i] + (sumB - sumA) // 2]


A = [1, 2, 5]
B = [2, 4]
solution = Solution()
print(solution.fairCandySwap(A, B))
