class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        res = []
        for str in strs:
            str_list = list(str)
            str_list.sort()
            key = ''.join(str_list)
            if key not in dict.keys():
                dict[key] = [str]
            else:
                dict[key].append(str)
        # print(dict)

        for value in dict.values():
            res.append(value)

        return res


strs = ['', '']
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
res = solution.groupAnagrams(strs)
print(res)
