class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key not in self.dict.keys():
            self.dict[key] = val
        else:
            del self.dict[key]
            self.dict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum = 0
        for key in self.dict.keys():
            if key.startswith(prefix):
                sum += self.dict[key]
        return sum


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('apple', 3)
print(obj.sum('ap'))
obj.insert('app', 2)
print(obj.sum('appl'))
