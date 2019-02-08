class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s_list = S.split()
        res = []
        for i in range(0, len(s_list)):
            first_letter = s_list[i][0]
            if s_list[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                temp = s_list[i] + 'ma'
            else:
                temp = s_list[i][1:] + first_letter + 'ma'

            for j in range(0, i + 1):
                temp += 'a'
            res.append(temp)

        res_str = ' '.join(res)

        return res_str


S = 'The quick brown fox jumped over the lazy dog'
solution = Solution()
res = solution.toGoatLatin(S)
print(res)
