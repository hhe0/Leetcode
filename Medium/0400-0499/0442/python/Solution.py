class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        i = 0
        while True:
            if i > len(nums) - 1:
                break

            if nums[i] != i+1:
                if nums[nums[i]-1] != nums[i]:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
                else:
                    # print(nums, i)
                    if nums[i] not in res:
                        res.append(nums[i])
                    i += 1
            else:
                i += 1

        return res


nums = []
solution = Solution()
res = solution.findDuplicates(nums)
print(res)