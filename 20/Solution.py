class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif i == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif i == '}':
                if not stack or stack.pop() != '{':
                    return False

        return True if not stack else False


s = '{[]}{}'
solution = Solution()
print(solution.isValid(s))

