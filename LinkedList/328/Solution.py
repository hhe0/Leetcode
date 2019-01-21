# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        temp = head.next
        even = head
        odd = head.next
        ptr = head

        i = 1
        while ptr:
            if i == 1 or i == 2:
                ptr = ptr.next
                i += 1
                continue
            if i % 2 == 1:
                even.next = ptr
                even = even.next
                ptr = ptr.next
            else:
                odd.next = ptr
                odd = odd.next
                ptr = ptr.next
            i += 1
        even.next = None
        odd.next = None

        even.next = temp

        return head


head = ListNode(1)
# node1 = ListNode(2)
# node2 = ListNode(3)
# node3 = ListNode(4)
# node4 = ListNode(5)

# head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4

solution = Solution()
res = solution.oddEvenList(head)
while res:
    print(res.val)
    res = res.next
