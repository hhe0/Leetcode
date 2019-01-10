# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


LinkList1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(4)
LinkList1.next = n1
n1.next = n2

solution = Solution()
solution.deleteNode(n1)

while LinkList1:
    print(LinkList1.val)
    LinkList1 = LinkList1.next

