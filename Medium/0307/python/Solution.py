class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if i < 0 or i > len(self.nums) - 1:
            return None

        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or j > len(self.nums) - 1:
            return None

        sum = 0
        for n in range(i, j+1):
            # print(nums[n])
            sum += self.nums[n]

        return sum

# Your NumArray object will be instantiated and called as such:


nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
