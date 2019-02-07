class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters:
            return None

        sub = ord('z') - ord('a')
        ch = ''
        for letter in letters:
            if ord(letter) > ord(target) and ord(letter) - ord(target) < sub:
                sub = ord(letter) - ord(target)
                ch = letter
        if not ch:
            return letters[0]

        return ch


letters = ['a', 'l']
target = 'm'
solution = Solution()
res = solution.nextGreatestLetter(letters, target)
print(res)
