class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_once = False
        l_once = False
        l_twice = False

        for ch in s:
            if ch == 'A':
                if a_once:
                    return False
                a_once = True
                l_once = False
                l_twice = False
            elif ch == 'L':
                if l_twice:
                    return False
                if l_once:
                    l_twice = True
                else:
                    l_once = True
            else:
                l_once = False
                l_twice = False

        return True


s = 'PPALLL'
solution = Solution()
res = solution.checkRecord(s)
print(res)