class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        for email in emails:
            index1 = email.index('+')
            index2 = email.index('@')
            res.append((email[:index1]).replace('.', '') + email[index2:])

        return len(set(res))


solution = Solution()
print(solution.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
