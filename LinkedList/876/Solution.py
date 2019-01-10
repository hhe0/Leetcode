# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = 0
        ptr = head
        while ptr:
            num += 1
            ptr = ptr.next

        pos = (num // 2) + 1

        i = 1
        while i < pos:
            head = head.next
            i += 1

        list = []
        while head:
            list.append(head.val)
            head = head.next

        return list


node = ListNode(1)
n1 = ListNode(2)
node.next = n1
n2 = ListNode(3)
n1.next = n2
n3 = ListNode(4)
n2.next = n3
n4 = ListNode(5)
n3.next = n4
# n5 = ListNode(6)
# n4.next = n5

solution = Solution()
print(solution.middleNode(node))
