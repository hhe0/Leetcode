class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.list = []
        self.size = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.list = [value] + self.list
            return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.list.append(value)
            return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.list.remove(self.list[0])
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.list.pop()
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if len(self.list):
            return self.list[0]
        else:
            return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if len(self.list):
            return self.list[len(self.list) - 1]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return True if not len(self.list) else False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return True if len(self.list) == self.size else False

# Your MyCircularDeque object will be instantiated and called as such:


obj = MyCircularDeque(4)
print(obj.insertFront(9))
print(obj.deleteLast())
print(obj.getRear())
print(obj.getFront())
print(obj.getFront())
print(obj.deleteFront())
print(obj.insertFront(6))
print(obj.insertLast(5))
print(obj.insertFront(9))
print(obj.getFront())
print(obj.insertFront(6))

