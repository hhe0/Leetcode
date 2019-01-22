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
        num1 = 0
        num2 = 0

        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        num = num1 + num2
        numStr = str(num)
        head = ListNode(0)
        tail = head

        for num in numStr:
            temp = ListNode(num)
            tail.next = temp
            tail = tail.next

        return head.next


n1 = ListNode(7)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(4)
n2.next = n3
n4 = ListNode(3)
n3.next = n4

m1 = ListNode(5)
m2 = ListNode(6)
m1.next = m2
m3 = ListNode(4)
m2.next = m3

solution = Solution()
res = solution.addTwoNumbers(n1, m1)

while res:
    print(res.val)
    res = res.next
