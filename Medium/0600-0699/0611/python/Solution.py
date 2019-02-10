class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        res = 0
        for i in range(len(nums) - 1, 1, -1):
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    res += (end - start)
                    end -= 1
                else:
                    start += 1

        return res


nums = [2, 2, 3, 4]
solution = Solution()
res = solution.triangleNumber(nums)
print(res)
