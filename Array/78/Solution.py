class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        for i in range(len(nums)):
            for j in range(len(res)):
                # 在原有集合的基础上加上一个元素
                res.append(res[j] + [nums[i]])

        return res

     dghfhgfhfgh
solution = Solution()
print(solution.subsets([1, 2, 3]))
