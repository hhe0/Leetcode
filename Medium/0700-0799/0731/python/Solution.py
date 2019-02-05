class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.order = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for ord in self.order:
            if not (start >= ord[1] or end <= ord[0]):
                return False

        for cal in self.calendar:
            if not (start >= cal[1] or end <= cal[0]):
                i = max(start, cal[0])
                j = min(end, cal[1])
                if i < j:
                    self.order.append([i, j])
        self.calendar.append([start, end])

        return True


# Your MyCalendarTwo object will be instantiated and called as such:

# ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
obj = MyCalendarTwo()
print(obj.book(47, 50))
print(obj.book(1, 10))
print(obj.book(27, 36))
print(obj.book(40, 47))
print(obj.book(20, 27))
print(obj.book(15, 23))
print(obj.book(10, 18))
print(obj.book(27, 36))
print(obj.book(17, 25))
print(obj.book(8, 17))
# print(obj.book(24, 33))
# print(obj.book(23, 28))
# print(obj.book(21, 27))
# print(obj.book(47, 50))
# print(obj.book(14, 21))
# print(obj.book(26, 32))
# print(obj.book(16, 21))
# print(obj.book(2, 7))
# print(obj.book(24, 33))
# print(obj.book(6, 13))
# print(obj.book(44, 50))
# print(obj.book(33, 39))
# print(obj.book(30, 36))
# print(obj.book(6, 15))
# print(obj.book(21, 27))
# print(obj.book(49, 50))
# print(obj.book(38, 45))
# print(obj.book(4, 12))
# print(obj.book(46, 50))
# print(obj.book(13, 21))


# [null,true,true,true,true,true,true,true,true,false,true, false,false,false,true,false,false,false,true,false,false,false,false,false,false,false,false,true,false,false,false]
# [null,true,true,true,true,true,true,true,true,false,false,false,false,false,true,false,false,false,true,false,false,false,false,false,false,false,false,true,false,false,false]