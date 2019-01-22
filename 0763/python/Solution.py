class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = 0
        res = []

        while n < len(S):
            i = n
            j = self.findMaxIndex(S, S[n])
            temp = ''
            while i <= j:
                temp += S[i]
                if i == j:
                    break
                j = max(j, self.findMaxIndex(S, S[i]))
                i += 1

            res.append(len(temp))
            n = i + 1

        return res

    def findMaxIndex(self, S, c):
        for i in range(len(S)-1, -1, -1):
            if S[i] == c:
                return i


S = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(S))
