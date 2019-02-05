class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []

        for num in nums1:
            index = nums2.index(num) + 1

            while index < len(nums2):
                if nums2[index] > num:
                    res.append(nums2[index])
                    break
                index += 1

            if index == len(nums2):
                res.append(-1)

        return res


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
solution = Solution()
res = solution.nextGreaterElement(nums1, nums2)
print(res)