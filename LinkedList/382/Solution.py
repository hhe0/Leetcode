import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        size = 0
        node = self.head
        while node:
            node = node.next
            size += 1

        node = self.head
        for _ in range(random.randint(0, size - 1)):
            node = node.next

        return node.val


# Your Solution object will be instantiated and called as such:
LinkList1 = ListNode(1)
n1 = ListNode(2)
LinkList1.next = n1
n2 = ListNode(3)
n1.next = n2
n3 = ListNode(4)
n2.next = n3
n4 = ListNode(5)
n3.next = n4
n5 = ListNode(6)
n4.next = n5

obj = Solution(LinkList1)
param_1 = obj.getRandom()
