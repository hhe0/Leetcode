class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums)):
            found = False
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    found = True
                    res.append(nums[j])
                    break

            if found:
                continue

            if not found:
                for k in range(0, i):
                    if nums[k] > nums[i]:
                        found = True
                        res.append(nums[k])
                        break
            if not found:
                res.append(-1)

        return res


nums = [1, 2, 1]
solution = Solution()
res = solution.nextGreaterElements(nums)
print(res)