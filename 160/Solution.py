# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == headB:
            return headA

        while headA:
            ptrB = headB
            while ptrB:
                if headA.next == ptrB.next:
                    return headA.next
                else:
                    ptrB = ptrB.next
            headA = headA.next

        return None


head1 = ListNode(2)
node1 = ListNode(6)
# node2 = ListNode(4)
head2 = ListNode(1)
# node4 = ListNode(5)

head1.next = node1
# node1.next = node2
head2.next = node1

solution = Solution()
res = solution.getIntersectionNode(head1, head2)
print(res.val)
