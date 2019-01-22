# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        len = 0
        while ptr:
            len += 1
            ptr = ptr.next
        pos = len + 1 - n

        if len == n:
            return head.next

        temp = head
        i = 1

        while i < pos - 1:
            temp = temp.next
            i += 1

        if temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None

        return head


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
n5 = ListNode(5)
n4.next = n5

solution = Solution()
res = solution.removeNthFromEnd(n1, 2)

while res:
    print(res.val)
    res = res.next

