class Solution:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.empty():
            return None

        val = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]

        return val

    def empty(self):
        if not self.stack:
            return True

    def len(self):
        if self.empty():
            return 0
        else:
            return len(self.stack)

    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        for ch in S:
            if ch == '(':
                self.push(ch)
            elif self.empty():
                count += 1
            else:
                self.pop()
        if not self.empty():
            count += self.len()

        return count


S = '(())())'
solution = Solution()
solution.minAddToMakeValid(S)

