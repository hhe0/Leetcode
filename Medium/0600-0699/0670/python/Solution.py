class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        li = list(s)
        li_sort = list(s)
        li_sort.sort(reverse=True)
        for i in range(0, len(li)):
            if li[i] != li_sort[i]:
                index = len(s) - 1 - s[::-1].index(li_sort[i])
                temp = li[i]
                li[i] = li[index]
                li[index] = temp
                break

        return int(''.join(li))


num = 9973
solution = Solution()
res = solution.maximumSwap(num)
print(res)
