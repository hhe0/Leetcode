class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.list.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        val = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]

        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.list):
            return self.list[len(self.list) - 1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.list) == 0

# Your MyStack object will be instantiated and called as such:


obj = MyStack()
obj.push('MyStack')
obj.push('empty')
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)