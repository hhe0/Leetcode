# Below is the interface for Iterator, which is already defined for you.


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.ptr = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.ptr < len(self.nums):
            return True
        else:
            return False

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            self.ptr += 1
            return self.nums[self.ptr - 1]
        else:
            return None


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterVal = iterator
        self.peekVal = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekVal and self.iterVal.hasNext():
            self.peekVal = self.iterVal.next()
        return self.peekVal

    def next(self):
        """
        :rtype: int
        """
        if not self.peekVal:
            return self.iterVal.next()
        else:
            res = self.peekVal
            self.peekVal = None
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peekVal or self.iterVal.hasNext():
            return True
        else:
            return False

# Your PeekingIterator object will be instantiated and called as such:


nums = [1, 2, 3]
# i = Iterator(nums)
# print(i.next())
# print(i.next())
# print(i.next())
# print(i.next())
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
    print(iter.next())
    print(iter.peek())
    print(iter.next())
    print(iter.next())
    print(iter.hasNext())
    print(iter.next())
    break
    # iter.next()         # Should return the same value as [val].
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     print(val)
#     iter.next()         # Should return the same value as [val].