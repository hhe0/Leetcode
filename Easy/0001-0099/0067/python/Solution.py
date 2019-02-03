class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        sum = ''

        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) + carry == 0:
                sum = '0' + sum
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 1:
                sum = '1' + sum
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 2:
                sum = '0' + sum
                carry = 1
            else:
                sum = '1' + sum
                carry = 1
            i -= 1
            j -= 1

        while i >= 0:
            if int(a[i]) + carry == 0:
                sum = '0' + sum
                carry = 0
            elif int(a[i]) + carry == 1:
                sum = '1' + sum
                carry = 0
            elif int(a[i]) + carry == 2:
                sum = '0' + sum
                carry = 1
            else:
                sum = '1' + sum
                carry = 1
            i -= 1

        while j >= 0:
            if int(b[j]) + carry == 0:
                sum = '0' + sum
                carry = 0
            elif int(b[j]) + carry == 1:
                sum = '1' + sum
                carry = 0
            elif int(b[j]) + carry == 2:
                sum = '0' + sum
                carry = 1
            else:
                sum = '1' + sum
                carry = 1
            j -= 1

        if carry:
            sum = '1' + sum

        return sum


a = '1111'
b = '1111'
solution = Solution()
res = solution.addBinary(a, b)
print(res)
