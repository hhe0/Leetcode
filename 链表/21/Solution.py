# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        ptr = head

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2

        return head.next


LinkList1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(4)
LinkList1.next = n1
n1.next = n2

LinkList2 = ListNode(1)
m1 = ListNode(3)
m2 = ListNode(4)
LinkList2.next = m1
m1.next = m2

solution = Solution()
a = solution.mergeTwoLists(None, LinkList2)
while a:
    print(a.val)
    a = a.next
