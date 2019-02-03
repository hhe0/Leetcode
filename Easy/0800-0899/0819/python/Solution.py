class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        new_paragraph = paragraph.replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ')
        new_list = new_paragraph.split(' ')
        # print(new_list)

        word_dict = {}
        for word in new_list:
            word = word.lower()
            if word == '':
                continue
            if word not in banned:
                if word not in word_dict.keys():
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1

        # print(word_dict)

        maxNum = 0
        maxWord = ''
        for key, value in word_dict.items():
            if value > maxNum:
                maxNum = value
                maxWord = key

        return maxWord


paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']
solution = Solution()
res = solution.mostCommonWord(paragraph, banned)
print(res)