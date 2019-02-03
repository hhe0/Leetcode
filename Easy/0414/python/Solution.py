class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_list = list(set(nums))
        nums_list.sort(reverse=True)
        # print(nums_list)
        
        if len(nums_list) >= 3:
            return nums_list[2]
        elif len(nums_list) > 0:
            return max(nums_list)
        else:
            return None


nums = [2, 2, 3, 1]
solution = Solution()
res = solution.thirdMax(nums)
print(res)

