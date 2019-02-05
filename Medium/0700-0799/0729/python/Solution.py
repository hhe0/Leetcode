class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        flag = True
        for cal in self.calendar:
            if not (start >= cal[1] or end <= cal[0]):
                flag = False
                break
        if flag:
            self.calendar.append([start, end])
            # print(self.calendar)
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
print(obj.book(5, 10))
print(obj.book(5, 30))
