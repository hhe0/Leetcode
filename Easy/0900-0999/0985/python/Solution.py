class Solution:
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        sum = 0
        for a in A:
            if a % 2 == 0:
                sum += a

        for query in queries:
            temp = A[query[1]] + query[0]
            if A[query[1]] % 2 == 1:
                if temp % 2 == 0:
                    sum += temp
            else:
                if temp % 2 == 1:
                    sum -= A[query[1]]
                else:
                    sum += query[0]
            A[query[1]] += query[0]
            res.append(sum)

        return res


A = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
solution = Solution()
res = solution.sumEvenAfterQueries(A, queries)
print(res)

