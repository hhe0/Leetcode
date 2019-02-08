class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ''

        if len(S) == 1:
            return S

        s = list(S)
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
                continue

            if not s[j].isalpha():
                j -= 1
                continue

            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1

        return ''.join(s)


S = 'Test1ng-Leet=code-Q!'
solution = Solution()
res = solution.reverseOnlyLetters(S)
print(res)
