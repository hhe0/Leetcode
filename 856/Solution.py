class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                if last == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * last
        return stack.pop()


S = '(()(()))'
solution = Solution()
res = solution.scoreOfParentheses(S)
print(res)

