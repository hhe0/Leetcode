class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
                continue
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
                continue

        return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
solution = Solution()
solution.intersect(nums1, nums2)