class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        li_A = A.split()
        li_B = B.split()

        dict_A = {}
        dict_B = {}
        for a in li_A:
            if a not in dict_A:
                dict_A[a] = 1
            else:
                dict_A[a] += 1
        for b in li_B:
            if b not in dict_B:
                dict_B[b] = 1
            else:
                dict_B[b] += 1

        res = []
        for ka, va in dict_A.items():
            if va == 1 and ka not in dict_B.keys():
                res.append(ka)
        for kb, vb in dict_B.items():
            if vb == 1 and kb not in dict_A.keys():
                res.append(kb)

        return res


A = ''
B = 'this  apple is sour'
solution = Solution()
res = solution.uncommonFromSentences(A, B)
print(res)
