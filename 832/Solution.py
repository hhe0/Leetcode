class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res_list = []
        for lists in A:
            tmp_list = []
            for list in lists[::-1]:
                if list == 1:
                    tmp_list.append(0)
                else:
                    tmp_list.append(1)
            res_list.append(tmp_list)

        return res_list


solution = Solution()
solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
