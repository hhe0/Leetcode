# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head

        ptr = new_head
        while ptr.next and ptr.next.next:
            a = ptr.next
            b = ptr.next.next
            ptr.next = b
            a.next = b.next
            b.next = a
            ptr = a

        return new_head.next


LinkList1 = ListNode(1)
n1 = ListNode(2)
# LinkList1.next = n1
# n2 = ListNode(3)
# n1.next = n2
# n3 = ListNode(4)
# n2.next = n3
# n4 = ListNode(5)
# n3.next = n4
# n5 = ListNode(6)
# n4.next = n5

solution = Solution()
res = solution.swapPairs(LinkList1)

while res:
    print(res.val)
    res = res.next


