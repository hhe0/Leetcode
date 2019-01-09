class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        print(nums1, nums2)
        list = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and num2 not in list:
                    list.append(num2)
                    break
        return list


solution = Solution()
solution.intersection([1, 2, 2, 3], [1, 2, 2, 3])
