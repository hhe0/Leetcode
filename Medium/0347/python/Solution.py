class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        res_list = []
        i = 1
        for lists in sorted_dict:
            if i <= k:
                res_list.append(lists[0])
                i += 1
            else:
                break

        return res_list


solution = Solution()
print(solution.topKFrequent([3, 3, 1, 2, 1, 2, 1, 3, 2, 2, 2], 2))

