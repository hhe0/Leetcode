class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.list.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            val = self.list[0]
            self.list.remove(self.list[0])
            return val

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.list[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if not self.list else False

# Your MyQueue object will be instantiated and called as such:


obj = MyQueue()
obj.push(2)
obj.push(3)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()