class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        max = 0
        for num, count in num_dict.items():
            if num+1 in num_dict.keys():
                temp = count + num_dict[num+1]
                if temp > max:
                    max = temp

        return max


nums = []
solution = Solution()
res = solution.findLHS(nums)
print(res)
