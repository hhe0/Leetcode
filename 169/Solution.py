class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_dict[0][0]


solution = Solution()
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
