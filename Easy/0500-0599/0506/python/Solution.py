import copy

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        temp = copy.copy(nums)
        nums.sort(reverse=True)

        dict = {}
        for i in range(0, len(nums)):
            if i == 0:
                dict[nums[0]] = 'Gold Medal'
            elif i == 1:
                dict[nums[1]] = 'Silver Medal'
            elif i == 2:
                dict[nums[2]] = 'Bronze Medal'
            else:
                dict[nums[i]] = str(i + 1)

        res = []
        for num in temp:
            res.append(dict[num])

        return res


nums = [10, 3, 8, 9, 4]
solution = Solution()
res = solution.findRelativeRanks(nums)
print(res)
