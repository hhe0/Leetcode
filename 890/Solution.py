class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pattern = self.getPattern(pattern)

        wordMap = []
        for word in words:
            wordMap.append(self.getPattern(word))

        res = []
        for k, r in enumerate(wordMap):
            if r == pattern:
                res.append(words[k])

        return res

    def getPattern(self, word):
        res = [0]
        count = 0
        i = 1
        while i < len(word):
            if word[i] != word[i - 1] and word.index(word[i]) == i:
                count = count + 1
            if word.index(word[i]) < i:
                res.append(word.index(word[i]))
            else:
                res.append(count)
            i += 1

        return res


words = ['abc', 'deq', 'mee', 'aqq', 'dkd', 'ccc']
pattern = 'abc'
solution = Solution()
print(solution.findAndReplacePattern(words, pattern))
