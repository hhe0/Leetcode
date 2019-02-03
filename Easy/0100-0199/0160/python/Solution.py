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
        if not headA or not headB:
            return None
        if headA == headB:
            return headA

        ptrA = headA
        lenA = 0
        while ptrA:
            lenA += 1
            ptrA = ptrA.next

        ptrB = headB
        lenB = 0
        while ptrB:
            lenB += 1
            ptrB = ptrB.next

        temp = abs(lenA - lenB)

        tempA = 0
        if lenA > lenB:
            while headA:
                tempA += 1
                if tempA > temp:
                    break
                headA = headA.next

        tempB = 0
        if lenB > lenA:
            while headB:
                tempB += 1
                if tempB > temp:
                    break
                headB = headB.next

        while headA and headB:
            if headA == headB:
                break
            headA = headA.next
            headB = headB.next

        if not headA or not headB:
            return None

        return headA


#   4 1 8 4 5
# 5 0 1 8 4 5
n0 = ListNode(2)
n1 = ListNode(6)
# n2 = ListNode(4)
# n3 = ListNode(1)
# n4 = ListNode(5)
# n5 = ListNode(3)
# n6 = ListNode(0)
# n7 = ListNode(1)

n0.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n5.next = n3
# n6.next = n7
# n7.next = n2
solution = Solution()
res = solution.getIntersectionNode(n1, n1)
print(res.val)
