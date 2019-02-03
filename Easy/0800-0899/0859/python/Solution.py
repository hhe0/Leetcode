class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            if len(set(list(A))) < len(list(A)):
                return True
            else:
                return False
        else:
            li = []
            list_A = list(A)
            list_B = list(B)

            for i in range(0, len(A)):
                if A[i] != B[i]:
                    li.append(i)
            if len(li) != 2:
                return False
            else:
                temp = list_A[li[0]]
                list_A[li[0]] = list_A[li[1]]
                list_A[li[1]] = temp

                if list_A != list_B:
                    return False

                return True


A = ''
B = 'aa'
solution = Solution()
res = solution.buddyStrings(A, B)
print(res)