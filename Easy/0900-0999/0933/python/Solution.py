class RecentCounter:

    def __init__(self):
        self.ping_list = []
        self.min_index = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_list.append(t)

        while t > self.ping_list[self.min_index] + 3000:
            self.min_index += 1

        return len(self.ping_list) - self.min_index


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
