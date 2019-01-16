class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        letter = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
            'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
            'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
        }
        for word in words:
            first = True
            val = 0
            flag = True
            for ch in word:
                if first:
                    val = letter[ch.lower()]
                    first = False
                else:
                    if val != 0 and letter[ch.lower()] != val:
                        flag = False
                        break
            if flag:
                res.append(word)

        return res


words = ["Hello", "Alaska", "Dad", "Peace"]
solution = Solution()
print(solution.findWords(words))

