# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        ptr = new_head

        while head:
            if head.val != val:
                ptr.next = head
                ptr = ptr.next
            head = head.next

        ptr.next = None

        return new_head.next


head = ListNode(0)
node1 = ListNode(1)
head.next = node1
node2 = ListNode(1)
node1.next = node2
node3 = ListNode(0)
node2.next = node3
node4 = ListNode(2)
node3.next = node4

solution = Solution()
res = solution.removeElements(head, 1)
while res:
    print(res.val)
    res = res.next
