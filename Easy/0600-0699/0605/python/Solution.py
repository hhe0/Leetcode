class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed:
            return False
        if not n:
            return True

        new_flowerbed = [0] + flowerbed + [0]
        # print(new_flowerbed)

        i = 1
        num = 0
        while i <= len(flowerbed):
            if not new_flowerbed[i] and not new_flowerbed[i-1] and not new_flowerbed[i+1]:
                # print(i, new_flowerbed[i])
                num += 1
                if num >= n:
                    return True
                i += 2
            else:
                i += 1

        return False


flowerbed = [1, 0, 1, 0, 1, 0, 1]
n = 0
solution = Solution()
res = solution.canPlaceFlowers(flowerbed, n)
print(res)
