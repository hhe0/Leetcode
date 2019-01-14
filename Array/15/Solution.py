class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        first = True
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        minNum = min(nums[i], nums[j], nums[k])
                        maxNum = max(nums[i], nums[j], nums[k])
                        otherNum = nums[i] + nums[j] + nums[k] - minNum - maxNum
                        print(minNum, otherNum, maxNum)
                        new = True
                        if first:
                            res.append(sorted([nums[i], nums[j], nums[k]]))
                            first = False
                        for r in range(len(res)):
                            if (minNum == res[0]) and (otherNum == res[1]) and (maxNum == res[2]):
                                new = False
                                break
                        if new:
                            res.append(sorted([nums[i], nums[j], nums[k]]))

        return res


solution = Solution()
print(solution.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))
