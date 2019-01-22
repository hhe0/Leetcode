# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tail = head
        last = 0

        while l1 and l2:
            if l1.val + l2.val + last >= 10:
                m = l1.val + l2.val + last - 10
                last = 1
            else:
                m = l1.val + l2.val + last
                last = 0

            temp = ListNode(m)
            tail.next = temp
            tail = tail.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            tail.next = l1
            while l1:
                tail = l1
                if l1.val + last >= 10:
                    l1.val = l1.val + last - 10
                    last = 1
                else:
                    l1.val += last
                    last = 0
                l1 = l1.next

        if l2:
            tail.next = l2
            while l2:
                tail = l2
                if l2.val + last >= 10:
                    l2.val = l2.val + last - 10
                    last = 1
                else:
                    l2.val += last
                    last = 0
                l2 = l2.next

        if last:
            temp = ListNode(1)
            tail.next = temp
            temp.next = None

        return head.next


n1 = ListNode(9)
n2 = ListNode(9)
n1.next = n2
# n3 = ListNode(3)
# n2.next = n3

m1 = ListNode(9)
# m2 = ListNode(3)
# m1.next = m2
# m3 = ListNode(4)
# m2.next = m3

solution = Solution()
res = solution.addTwoNumbers(n1, m1)

while res:
    print(res.val)
    res = res.next
