class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name or not typed:
            return False

        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if typed[j] == name[i]:
                i += 1
                j += 1
            elif typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        if i < len(name):
            return False

        return True


name = 'laiden'
typed = 'laiden'
solution = Solution()
res = solution.isLongPressedName(name, typed)
print(res)
