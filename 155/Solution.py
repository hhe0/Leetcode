class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min is None:
            self.min = x
        elif x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if len(self.stack) == 1:
                self.min = None
            else:
                self.min = min(self.stack[0:len(self.stack) - 1])
            return self.stack.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:

obj = MinStack()

obj.push(1)
# print(obj.getMin())
obj.push(0)
# print(obj.getMin())
obj.push(2)
obj.push(3)
obj.push(4)

obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.getMin())

# obj.push(3)
# print(obj.getMin())


# print(obj.getMin())
# print(obj.top())
# print(obj.pop())
#
# print(obj.getMin())
# print(obj.top())
# print(obj.pop())
#
# print(obj.getMin())
# print(obj.top())
# print(obj.pop())
#
# print(obj.getMin())
# print(obj.top())
# print(obj.pop())
#
# print(obj.getMin())
