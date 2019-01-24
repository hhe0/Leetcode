class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = 0
        sum = 0
        while i < len(s):
            if i < len(s) - 1:
                temp = s[i] + s[i+1]
                if temp in dict.keys():
                    sum += dict[temp]
                    i += 2
                else:
                    sum += dict[s[i]]
                    i += 1
            else:
                sum += dict[s[i]]
                i += 1

        return sum


s = 'MCMXCIV'
solution = Solution()
res = solution.romanToInt(s)
print(res)
