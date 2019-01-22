# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        list_start = []
        while head:
            list_start.append(head.val)
            head = head.next

        list_end = []
        dict = {}
        for i in range(len(list_start)):
            dict[(i + k) % len(list_start)] = i
            i += 1

        for i in range(len(list_start)):
            list_end.append(list_start[dict[i]])

        new_head = ListNode(0)
        tail = new_head

        for i in range(len(list_end)):
            temp = ListNode(list_end[i])
            tail.next = temp
            tail = tail.next

        return new_head.next


LinkList1 = ListNode(0)
n1 = ListNode(1)
LinkList1.next = n1
n2 = ListNode(2)
n1.next = n2
# n3 = ListNode(4)
# n2.next = n3
# n4 = ListNode(5)
# n3.next = n4

solution = Solution()
res = solution.rotateRight(LinkList1, 4)

while res:
    print(res.val)
    res = res.next
