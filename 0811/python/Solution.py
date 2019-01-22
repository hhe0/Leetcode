class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for cpdomain in cpdomains:
            num = int(cpdomain[0:cpdomain.index(' ')])
            domain = cpdomain[cpdomain.index(' ')+1:]
            temp = domain.split('.')
            s = ''
            i = len(temp) - 1
            while i >= 0:
                if i == len(temp) - 1:
                    s = temp[i]
                else:
                    s = temp[i] + '.' + s
                if s in dict.keys():
                    dict[s] += num
                else:
                    dict[s] = num
                i -= 1

        res = []
        for key in dict.keys():
            res.append(str(dict[key]) + ' ' + key)

        return res


cpdomains = ['900 google.mail.com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org']
solution = Solution()
res = solution.subdomainVisits(cpdomains)
print(res)
