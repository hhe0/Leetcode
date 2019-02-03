class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0


pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
solution = Solution()
solution.validateStackSequences(pushed, popped)
